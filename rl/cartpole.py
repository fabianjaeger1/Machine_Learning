import gymnasium as gym
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from collections import namedtuple, deque
import random

import matplotlib
import matplotlib.pyplot as plt

import torch.nn.functional as F

# Create an environment
env = gym.make("CartPole-v1")

device = torch.device(
  "cuda" if torch.cuda.is_available() else
  "mps" if torch.backends.mps.is_available() else 
  "cpu"
)

# set up matplotlib renderer
is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display

plt.ion()



# represents a single transition in our environment. Maps (state, action) pairs to (next_state, reward) result
Transition = namedtuple("Transition", ("state", "action", "next_state", "reward"))


class ReplayMemory:

  def __init__(self, capacity):
    self.memory= deque([], maxlen = capacity)

  def __len__(self):
    return len(self.memory)

  def push(self, *args):
    """Save a transition"""
    self.memory.append(Transition(*args))

  def sample(self, batch_size):
    return random.sample(self.memory, batch_size)


class DQN(nn.Module):

  def __init__(self, n_observations, n_actions):
    super(DQN, self).__init__()
    self.layer1 = nn.Linear(n_observations, 128)
    self.layer2 = nn.Linear(128, 128)
    self.layer3 = nn.Linear(128, n_actions)

  def forward(self, x):
    x = F.relu(self.layer1(x))
    x = F.relu(self.layer2(x))
    return self.layer3(x)