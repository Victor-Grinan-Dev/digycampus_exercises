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


    
if __name__ == '__main__':
    print(parhaat_tulokset('test_sessions.pkl'))
    # print(open_file('test_sessions.pkl'))
    # check_best_of_each(open_file('test_sessions.pkl'))
    # delete_file('test_sessions.pkl')
    # append_tiedostoon('test_sessions.pkl', data1)
