def truncate(text, lenght):
    if len(text) > lenght:
        return text[:lenght]+ '...'
print(truncate('hexlet' , 2))