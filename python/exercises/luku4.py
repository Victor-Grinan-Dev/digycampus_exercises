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
