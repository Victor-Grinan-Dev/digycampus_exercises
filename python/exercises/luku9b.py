import math
import pickle
import os
#ex.b1
def lue_sanakirja_tiedostosta(polku):
    with open(polku, 'rb') as file:
        d = pickle.load(file)
        for key, value in d.items():
            print((key, value))

#ex.b2
def kirjoita_tiedostoon(tiedosto, objektit):
    with open(tiedosto, 'wb') as file:
        for item in objektit:
            pickle.dump(item, file)

#ex.b3
data1=[{'Emmi': [5, 10, 5, 6], 'Simo': [5, 6, 6, 0], 'Timo': [10, 9, 9, 10]}, {'Emmi': [5, 5, 10, 7], 'Simo': [5, 0, 0, 6], 'Elli': [0, 8, 8, 8]}, {'Emmi': [10, 8, 6, 5], 'Simo': [10, 8, 0, 8], 'Elli': [0, 5, 5, 9]}, {'Kalle': [5, 5, 6, 0], 'Elli': [7, 7, 10, 6]}]
data2 = [{'Tiina': [5, 10, 5, 6], 'Simo': [10, 9, 9, 6], 'Timo': [10, 9, 9, 10]}, {'Emmi': [5, 5, 10, 7], 'Simo': [5, 0, 0, 6], 'Elli': [0, 8, 8, 8]}, {'Silja': [10, 5, 4, 0], 'Simo': [10, 8, 0, 8], 'Elli': [0, 5, 5, 9]}, {'Kalle': [5, 5, 6, 0], 'Aatu': [7, 7, 10, 6]}]

def delete_file(tiedosto):
    os.remove(tiedosto)

def append_tiedostoon(tiedosto, objektit):
    with open(tiedosto, 'ab') as file:
        for item in objektit:
            pickle.dump(item, file)

# for i in data1:
#     append_tiedostoon('test_sessions.pkl', i)
            
def open_file(polku):#multiple lines
    try:
        with open(polku, 'rb') as file:
            test_sessions = []
            while True:
                try:
                    test_session = pickle.load(file)
                    test_sessions.append(test_session)
                except:
                    break
            # print(test_sessions)
            return test_sessions
    except FileNotFoundError as e:
        return e

def compare_scores(score_list1:list, score_list2:list):
    if sum(score_list1) > sum(score_list2):
        return score_list1
    else:
        return score_list2

def parhaat_tulokset(polku):
    data = open_file(polku)
    best_attempt = {}
    for session in data:
        for student, results in session.items():
            if student in best_attempt:
                best_attempt[student] = compare_scores(best_attempt[student], results)
            else:
                best_attempt[student] = results
    return best_attempt

    # print(open_file('test_sessions.pkl'))
    # check_best_of_each(open_file('test_sessions.pkl'))
    # delete_file('test_sessions.pkl')
    # append_tiedostoon('test_sessions.pkl', data1)

#ex4b
result=-1
first_round=True
rec_type = ''

def rec_hae(lista:list, haku:int):

    global result
    global first_round
    global rec_type

    lista.sort()
    max_idx = len(lista)-1
    middle_idx = max_idx//2
    middle_value = lista[middle_idx]

    if not first_round:
        # print('-> ' if middle_value < haku else '<- ', end='')
        print(rec_type, end=' ')
    print(f"l: {lista} haku: {haku} mid: {middle_value} (i:{middle_idx})")
    if middle_value > haku:
        rec_type = '<-'
    else:
        rec_type = '->'
    first_round = False
    if middle_value == haku: 
        result = middle_value
        first_round=True
        return 
    
    elif max_idx >= 1 and middle_value > haku: #left recurssion
        rec_hae(lista[:middle_idx], haku)

    elif max_idx >= 1 and middle_value < haku: #right recurssion
        rec_hae(lista[middle_idx+1:], haku)
        
    else:
        print(rec_type, end=' ')
        result=-1
    first_round=True
    return result
    
     



def test9b4():
    print('(alku)',end=' ')
    sarja = [2, 3, 4, 6, 6, 8, 9, 10, 10, 12]
    # sarja =  [2, 3, 4, 6, 5, 8, 9, 10, 10, 12]
    palautus = rec_hae(sarja, 5)
    if palautus != -1:
        print('löytyi:', palautus)
    else:
        print('ei löytynyt')
    # (alku) l: [2, 3, 4, 6, 6, 8, 9, 10, 10, 12] haku: 5 mid: 6 (i:4)
    # <- l: [2, 3, 4, 6] haku: 5 mid: 3 (i:1)
    # -> l: [4, 6] haku: 5 mid: 4 (i:0)
    # -> l: [6] haku: 5 mid: 6 (i:0)
    # <- ei löytynyt

if __name__ == '__main__':
    test9b4()

