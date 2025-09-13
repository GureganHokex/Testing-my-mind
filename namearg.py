text = 'python'

def trim_and_repeat(text, offset, repetitions):
    return text[offset:]*repetitions
print(trim_and_repeat(text,0 ,  2))