#Note: The openai-python library support for Azure OpenAI is in preview.
import os
from openai import OpenAI, types

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
def split_paragraphs(filePath: str = None):
    loader = TextLoader("sample1.txt" if filePath is None else filePath, encoding="utf-8")
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
    return text_chunk_list


from pathlib import Path
def split_paragraphs2(filePath: str = None):
    input_full = Path(filePath).read_text()
    list_paragraphs = list(filter(lambda x : x != '', input_full.split('\n\n')))
    return list_paragraphs

def generate_system_message() -> str:
    return """
You are a data scientist working for a company that is building a graph database. Your task is to extract information from data and convert it into a graph database.
Provide a set of Nodes in the form [ENTITY_ID, TYPE, PROPERTIES] and a set of relationships in the form [ENTITY_ID_1, RELATIONSHIP, ENTITY_ID_2, PROPERTIES].
It is important that the ENTITY_ID_1 and ENTITY_ID_2 exists as nodes with a matching ENTITY_ID. If you can't pair a relationship with a pair of nodes don't add it.
When you find a node or relationship you want to add try to create a generic TYPE for it that  describes the entity you can also think of it as a label.

Example:
Data: Alice lawyer and is 25 years old and Bob is her roommate since 2001. Bob works as a journalist. Alice owns a the webpage www.alice.com and Bob owns the webpage www.bob.com.
Nodes: ["alice", "Person", {"age": 25, "occupation": "lawyer", "name":"Alice"}], ["bob", "Person", {"occupation": "journalist", "name": "Bob"}], ["alice.com", "Webpage", {"url": "www.alice.com"}], ["bob.com", "Webpage", {"url": "www.bob.com"}]
Relationships: ["alice", "roommate", "bob", {"start": 2021}], ["alice", "owns", "alice.com", {}], ["bob", "owns", "bob.com", {}]
"""

def generate_prompt(data) -> str:
    return f"""
Data: {data}"""

def GetContentFromChatCompletion(response: types.chat.chat_completion.ChatCompletion):
    output_model = response.choices[0].message.content
    output_formatted = output_model.replace('\\n', '\n').replace('\\t', '\t')
    return output_formatted



client = OpenAI(base_url="http://xps15:1234/v1", api_key="not-needed")
'''
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
    },
    {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
 ]
'''

filePath = r'C:\WORK\workroom\python\pythonWorkroom\pgvector\lease-11-1958.txt'
list_ps = split_paragraphs2(filePath)

#for paragraph in list_ps:
paragraph1 = list_ps[0]
messages = [
        {"role": "system", "content": generate_system_message()},
        {"role": "user", "content": generate_prompt(paragraph1)},
    ]
print(messages)

response = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages = messages,
  temperature=0,
  max_tokens=350,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

output_formatted = GetContentFromChatCompletion(response)
print(output_formatted)


