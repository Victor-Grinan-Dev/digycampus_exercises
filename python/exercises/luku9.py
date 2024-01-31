import pickle
myset = {1, 2, 3}
mylist = [2, 3]
myset.add(3) 
# print(myset)
# print(len(myset))
myset2 = set(mylist)
def pickle_sample():
    print(myset)
    'pickle.dump(), pickle.load()'
    'numpy, pandas'

    # with open('test.pkl', 'wb') as file:
    #     pickle.dump({'name':'victor', 'age':40}, file)

    # with open('test.pkl', 'rb') as file:
    #     d = pickle.load(file)
    #     print(d)

    print(myset2.issubset(myset))
    print(myset.issuperset(myset2))

#ex.1
def ex_1():
    lisattavat = ["toinen", "testikierros", "lisää sekalaisia juttuja", 2353, True, "moi"]
    numerot = {i for i in range(1,11)}
    numerot.remove(6)
    numerot.update(lisattavat)
    print(numerot)

#ex.2
def ex_2():
    
ex_2()