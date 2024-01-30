#ex1
def ex_1():
    teksti = 'Hello World!'
    kirjaimet:str

    a = 'Hello'
    b = ' '
    c = 'World!'
    yhdiste = a + b + c
    print(yhdiste)

    for i in range(len(teksti) ):
        print(teksti[i])

    for i in range(len(teksti)):
        if teksti[i] != ' ':
            kirjaimet+=teksti[i]

#ex2
def tarkista_merkkijono(x:str):
    result = []
    special_char = True
    # Does the string contain only letters or numbers?
    result.append(x.isalnum())
    result.append(x.isalpha())
    result.append(x.isnumeric())
    result.append(x.islower())
    for i in range(len(x)):
        if not x.strip():
            break
        elif x[i].isalpha or x[i].isnumeric:
            special_char = False
            break
    result.append(special_char)
    result.append(x.isupper())
    return result

#ex3