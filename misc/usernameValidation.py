import re

def CodelandUsernameValidation(strParam):
  if (not((len(strParam)>= 4) and (len(strParam) <=25))):
    return "false"
  m = re.search("^[a-zA-Z]+[a-zA-Z_]*[^_]+$", strParam)
  if m:
    return "true"
  else:
    return "false"
  
  # code goes here
  return strParam

# keep this function call here 
print(CodelandUsernameValidation(input()))