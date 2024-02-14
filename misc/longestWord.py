import re

def LongestWord(sen):

  # code goes here
  words = re.findall(r'[a-zA-Z]*', sen)
  filteredWords = filter(lambda w: len(w)>0 , words)
  return sorted(filteredWords, key=len, reverse=True)[0]

# keep this function call here 
print(LongestWord(input()))