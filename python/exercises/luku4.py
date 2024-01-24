
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
    x=5
    y=7
    for _ in range(x):
        for _ in range(y):
            print('*', end='')
        print()
#ex.6
def ex4_6():
    alku = 1
    ylaraja = 1005
    fibonacci_a = 13
    fibonacci_b = 21

    value = 1000
    for i in range(1001, ylaraja + 1):
        value += i

    print(f"1 : {value}")

    for i in range(alku, alku + 101):
        if i % 5 == 0 and i % 7 == 0:
            print(f"2: {i}")

        
    fib_sequence = [fibonacci_a, fibonacci_b]

    # Generate Fibonacci sequence using a for loop
    for i in range(5):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
        print(f'3: {next_term}') 
#ex.7
def ex4_7():
    korkoprosentti = 12 
    rahat=168 
    vuodet = 1
    Alkupääoma = rahat
    while vuodet < 5:
        rahat += rahat*korkoprosentti/100
        vuosikertyma =  rahat - Alkupääoma
        print(f'{vuodet} vuoden jälkeen, rahat: {format(rahat, ".2f")} vuosikertymä: {format(vuosikertyma, ".2f")}') 
        Alkupääoma = rahat
        vuodet += 1

#ex.8
def ex4_8():
    for _ in range(5):
        for _ in range(5):
            print('*', end='')
        print()  
    print()
    for i in range(5):
        for j in range(5-i):
            print('*',end='')
        print()

    for i in range(1,10):
        if i <= 5:
            for _ in range(i):
                print('*', end='')
        else:
            for _ in range((i-10 )* -1):
                print('*', end='')
        print()
    print()
    for i in range(5):
        if i < 3:
            for j in range(5):
                if i == j or i + j == 5 - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        elif i > 2:  
            for j in range(5):
                if i == j or i + j == 5 - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()
#ex.9 
def ex4_9():
    pass         

#ex.10
def ex4_10():
    pass            


ex4_8()
