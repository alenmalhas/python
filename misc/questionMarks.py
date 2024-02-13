import re

def QuestionsMarks(s): 
    compare=0
    for i in s:
        if i.isdigit()==True and compare+int(i)==10:
            
            if s[s.index(str(compare)):s.index(i)].count("?")==3:
                return "true"
        elif i.isdigit()==True:
            compare=int(i)
    return "false"

def QuestionsMarks2(s):
    patternStartIndex = 0
    patternStartDigit = -1
    patternEvalResultList = []
    for curIndex in range(len(s)):
        curChar = s[curIndex]
        if curChar.isdigit() and patternStartDigit + int(curChar) == 10:
            pattern = s[patternStartIndex:curIndex]
            if pattern.count("?") == 3:
                patternEvalResultList.append(True)
                patternStartIndex = curIndex
                patternStartDigit = int(curChar)
            else:
                return "false"
        elif curChar.isdigit():
            patternStartIndex = curIndex
            patternStartDigit = int(s[curIndex])
    
    return "true" if len(patternEvalResultList)>0 and all(patternEvalResultList) else "false"



# keep this function call here 
print(QuestionsMarks2(input()))