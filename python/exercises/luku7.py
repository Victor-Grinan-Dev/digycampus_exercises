#ex.1
# Lst[ Initial : End : IndexJump ]
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
ex4()