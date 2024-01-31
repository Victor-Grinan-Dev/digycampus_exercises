import pickle
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
    
def check_best_of_each(test_sessions):
    best_attempt = {}
    for name in test_sessions:
        print(name)

# open_file('test_sessions.pkl')
check_best_of_each(open_file('test_sessions.pkl'))