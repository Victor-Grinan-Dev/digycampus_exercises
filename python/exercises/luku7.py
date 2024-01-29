#ex.1
# Lst[ Initial : End : IndexJump ]
import math
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
    for item in haettava :
        for index in range(len(aineisto)):
            if aineisto[index] == item:
                result.append(index)
    result.sort()
    return result

#ex.9
pisteet = [
    ['Pirkko', 91.95, 31.72, 31.05],
    ['Leena', 14.72, 16.63, 80.59, 38.69, 51.85],
    ['Maarit', 61.15, 84.1, 81.17],
    ['Sami', 60.96],
    ['Elisabet', 75.66, 80.76, 45.48],
    ['Johannes', 53.5, 90.6, 27.04, 84.06],
    ['Kalervo', 24.35],
    ['Kyllikki', 87.86, 64.44],
    ['Sari', 78.78, 68.66],
    ['Jaakko', 47.98, 21.44, 61.46, 80.28, 7.26],
    ['Henrik', 73.19, 40.39],
    ['Minna', 77.17, 80.78],
    ['Heikki', 22.36, 82.82],
    ['Pekka', 30.8, 83.38, 68.0],
    ['Päivi', 46.39, 96.05, 87.75, 6.68],
    ['Ari', 8.21],
    ['Petteri', 10.6, 84.56, 10.64, 1.84],
    ['Helena', 63.45, 34.35, 23.65, 97.23],
    ['Marika', 34.89],
    ['Ville', 29.06, 11.03, 65.78, 76.9, 93.65],
]
def lapipaasseet(henkilot_ja_pisteet, pisteraja): 
    tuloslista = []
    for element in henkilot_ja_pisteet:
        nimi = element[0]
        pisteet = element[1:] 
        total = 0
        for piste in pisteet:
            total += piste	
            if total >= pisteraja:
                tuloslista.append(nimi)
                break
    return tuloslista
def paras(henkilot_ja_pisteet): 
    result = []
    paras = 0
    for element in henkilot_ja_pisteet:
        nimi = element[0]
        pisteet = element[1:] 
        total = 0
        for piste in pisteet:
            total += piste	
         
        if total > paras:
            paras = total
            result = [nimi, round(total, 2)]
         
    return tuple(result)

# print(lapipaasseet(pisteet))
lapipaasseet(pisteet, 100)
print(paras(pisteet))
