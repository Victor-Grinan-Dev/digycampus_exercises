
from random import randint

#ex.1
def ex4_1():
    start = 4
    stop = 24
    step = 1

    for i in range(stop):
        print(f'{i} / {stop}')
        
    for i in range(start, stop):
        print(f'{i} / {stop}')
        
    for i in range(start, stop, step):
        print(f'{i} / {stop}')
#ex.2
def ex4_2():
        askel = 2
        for i in range(50,61):
            print(f'{i}')
        
        for i in range(0,21):
            if i % 3 == 0:
                print(f'{i}')
     
        for i in range(1,100, askel):
            if i % 3 == 0:
                print(f'{i}')

#ex.3
def ex4_3():
    x = 0
    y= 99
    i = 10
    j = 6
    while x < 100:
        print(1, x)
        x += y
    
    while i >= j:
        print(2, i)
        i -= 1
#ex.4
def ex4_4():
    A=50
    B=55
    i = 1

    while True:
        num = randint(1, 100)
        if num == B:
            print('B löytyi!')
            break
        elif num == A:
            print('A löytyi!')
            continue
        i += 1
    print(i)

#ex.5
def ex4_5():
    pass
#ex.6
def ex4_6():
    pass
#ex.7
def ex4_7():
    pass
#ex.8
def ex4_8():
    pass
#ex.9 
def ex4_9():
    pass             
#ex.10
def ex4_10():
    pass            


ex4_4()