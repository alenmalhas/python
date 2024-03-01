#Note: The openai-python library support for Azure OpenAI is in preview.
import os
from openai import OpenAI


client = OpenAI(base_url="http://xps15:1234/v1", api_key="not-needed")
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
    },
    {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
 ]

from pathlib import Path
input_full = Path(r'C:\WORK\workroom\python\pythonWorkroom\pgvector\lease-11-1958.txt').read_text()

list_paragraphs = list(filter(lambda x : x != '', input_full.split('\n\n')))


response = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages = messages,
  temperature=0,
  max_tokens=350,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

output_model = response.choices[0].message.content
output_formatted = output_model.replace('\\n', '\n').replace('\\t', '\t')

print(output_formatted)


def test1():
    '''
    loader = TextLoader("lease-11-1958.txt", encoding="utf-8")
    raw_doc_list = loader.load()
    #print(len(docs))
    #text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=80)
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
    model_output_embeddings = QueryModelWithTextChunks(text_chunk_list)
    '''