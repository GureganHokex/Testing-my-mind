def get_hidden_card(numb, star=4): #2034399002121100 номер карты, должно показать только последние 4 цифры
    return '*'*star+numb[-star:]
print(get_hidden_card('2034399002121100',3))