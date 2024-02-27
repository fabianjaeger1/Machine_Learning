import os
import csv
from langchain.docstore import Document

from constants import (
    DOCUMENT_MAP
)


def load_documents(src_dir: str) -> list[Document]:
    '''Loads all files from the source directory as well as any nested directories'''
    paths = []
    
    
    # Walk the directories and append any documents that match the DOCUMENT_MAP constant document types
    for root, _, files in os.walk(src_dir):
        for file_name in files:
            print("Importing " + file_name)
            file_ext = os.path.splitext(file_name)[1]
            src_file_path = os.path.join(root, file_name)
            if file_ext in DOCUMENT_MAP.keys():
                paths.append(src_file_path)
    
    
    
