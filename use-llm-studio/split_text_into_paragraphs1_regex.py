import fileinput
import re
from pathlib import Path

NEWLINES_RE = re.compile(r"\n{2,}")  # two or more "\n" characters

def split_paragraphs(input_text=""):
    no_newlines = input_text.strip("\n")  # remove leading and trailing "\n"
    split_text = NEWLINES_RE.split(no_newlines)  # regex splitting

    paragraphs = [p + "\n" for p in split_text if p.strip()]
    # p + "\n" ensures that all lines in the paragraph end with a newline
    # p.strip() == True if paragraph has other characters than whitespace

    return paragraphs

'''
# sample code, to split all script input files into paragraphs
text = "".join(fileinput.input())
for paragraph in split_paragraphs(text):
    print(f"<<{paragraph}>>\n")
'''

# ref: https://stackoverflow.com/questions/3758147/easiest-way-to-read-write-a-files-content-in-python
#with open(r'C:\WORK\workroom\python\pythonWorkroom\pgvector\lease-11-1958.txt') as f: input_file_content = f.read()

file_path = r'C:\WORK\workroom\python\pythonWorkroom\pgvector\lease-11-1958.txt'
input_file_content = Path(file_path).read_text()
list_paragraphs = split_paragraphs(input_file_content)
print(list_paragraphs)



