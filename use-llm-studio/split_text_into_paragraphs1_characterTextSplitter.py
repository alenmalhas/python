from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter

from pathlib import Path
from dotenv import load_dotenv

'''
import os
#load_dotenv()
BASE_DIR = os.getcwd() #Path(__file__).parents[1]
DB_INIT_FILE = BASE_DIR +'/database.ini'
'''

def split_paragraphs(filePath: str = None):

    loader = TextLoader("lease-11-1958.txt" if filePath is None else filePath, encoding="utf-8")
    raw_doc_list = loader.load()
    #text_splitter2 = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=80)
    text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    doc_chunk_list = text_splitter.split_documents(raw_doc_list)
    text_chunk_list = [c.page_content for c in doc_chunk_list]
    load_dotenv()
    #model_output_embeddings = QueryModelWithTextChunks(text_chunk_list)
    return text_chunk_list


ret1 = split_paragraphs(r'C:\WORK\workroom\python\pythonWorkroom\pgvector\lease-11-1958.txt')
print(ret1)
