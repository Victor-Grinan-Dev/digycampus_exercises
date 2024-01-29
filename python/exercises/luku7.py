#ex.1
# Lst[ Initial : End : IndexJump ]
import random


def ex1():
    apinat =  ['apina', 'gorilla', 'simpanssi', 'ihminen', 'bonobo', 'oranki', 'hulokki', 'gibboni']
 
    print(apinat[0])
    print(apinat[1])
    print(apinat[-2])
    print(apinat[:3])
    print(apinat[-2:])
    print(apinat[1:5])

#ex.2
def ex2():
    print(list('aeiouyåäö'))
    print(list(range(2,21,2)))


#ex.3
def ex3():
    for i in list_apinat:
        print(i)
        
    for i in list_apinat:
        if i == 'gorilla' or i == 'oranki':
            print(i)

#ex.4
def ex4():  	
    lista_a = ["omena", "banaani", "ananas"]
    lista_b = ["apina", "gorilla", "simpanssi", "simpanssi"]
    lista_c = ["koira", "kissa", "papukaija"]
    lista_d = ["delfiini", "valas", "tonnikala"]

    lista_a.extend(['Pekka', 'Haavisto'])
    lista_b.remove('simpanssi')
    lista_e = lista_b
    lista_e.extend(lista_c)
    lista_e.extend(lista_d)
    lista_e.sort()

    print(len(lista_a))
    #Lista A pituus : 5↩
    print(lista_b)
    #Lista B : ['apina', 'gorilla', 'simpanssi']↩
    print(lista_c)
    #Lista C : ['koira', 'kissa', 'papukaija']↩
    print(lista_d)
    #Lista D : ['delfiini', 'valas', 'tonnikala']↩
    print(lista_e)
    #Lista E : ['apina', 'delfiini', 'gorilla', 'kissa', 'koira','papukaija', 'simpanssi', 'tonnikala', 'valas']
#ex.5
def ex5():  	

    random.seed(50)
    arvosanat = list()
    nimet = ['Anna', 'Antti', 'Cecilia', 'Emma', 'Eetu', 'Heikki', 'Janna']
    for _ in range(15):
        nimi = random.choice(nimet)
        arvosana = random.randint(0,5)
        arvosanat.append([nimi,arvosana])

    vitosia = 0 
    emmoja = 0

    for record in arvosanat:
        if record[0] == 'Emma':
            emmoja += 1
        if record[1] == 5:
            vitosia += 1
#ex.6
def ex6():  	
    tilaajat = ['Matti Mallikas', 'Simo Särmä', 'Tiina Terävä']
    numerot = tuple(i for i in range(1,11))
    mallinumero = tuple([4930])
    tuple_tilaajat = tuple(tilaajat )
    print(type(numerot))
    print(type(mallinumero))
    print(type(tuple_tilaajat))
#ex.7
def unique_count7(lista):  	
    return len(dict.fromkeys(lista))

#ex.8
ainesto = ['mölyapina', 'kummituseläin', 'marakatti', 'bonobo','marakatti', 'mölyapina', 'oranki', 'kummituseläin', 'marakatti', 'apina','ihminen', 'kummituseläin', 'apina', 'bonobo', 'marakatti']
def kaikki8(aineisto, haettava):
    
    result = []
    for element in aineisto :
        for item in haettava:
            if element == item:
                result.append(aineisto.index(element))
    return result

def ex8():  	
    pass

print(kaikki8(ainesto, ['marakatti', 'mölyapina',]))