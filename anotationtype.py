text = 'python'

def letter_multiply(text:str,letter:str,multy:int)->str:
    return text.replace(letter,str(multy*letter))
print(letter_multiply(text,'h',3))