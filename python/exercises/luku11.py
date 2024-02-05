#ex.1
class Person:
    def __init__(self, person_id, first_name, last_name):
        self.id = person_id
        self.first_name = first_name
        self.last_name = last_name

    def say_hi(self):
        print(self.first_name,'says hi!')
        
        
class Student(Person):
    def __init__(self, person_id, first_name, last_name, student_id):
        super().__init__(person_id, first_name, last_name)
        self.student_id = student_id
    
    def study(self):
        print(f"{self.first_name} studies hard!")

#ex.2
class Tili:
    __last_access = ""
    
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__funds = 0

    def get_funds(self):
        return self.__funds 

    def set_funds(self, funds):
        self.__funds = funds

    def check_last_login(self):
        print(self.__last_access)

    def set_funds(self, funds):
        self.__funds = funds

    def deposit(self, funds):
        self.__funds += funds

    def withdraw(self, funds):
        if funds > self.__funds:
            print("Insufficient funds")
            return 0
        else:
            self.__funds -= funds
            return funds
        
    def print_statement(self):
        print(f"""\n======== Bank Statement ========
Account {self.__account_number}
Current balance: {self.__funds} €""")
        
class Luottotili(Tili):
    def __init__(self, __account_number, credit_limit):
        super().__init__(__account_number)
        self.__credit_limit = credit_limit
 
    def withdraw(self, funds):
        if self._Tili__funds <= 0 and self._Tili__funds - funds >= (self.__credit_limit * -1):
            self._Tili__funds -= funds
            return self._Tili__funds
        else:
            print("Insufficient funds")
            return 0


def test_ex_2():
    tili_b = Luottotili("FI495512295420503520", 5000)
    tili_b.withdraw(500)
    tili_b.deposit(200)
    tili_b.print_statement()
    if issubclass(Luottotili,Tili):
        print('Luottotili on Tili-luokan aliluokka')
    else:
        print('Luottotili ei ole Tili-luokan aliluokka!!')

if __name__ == '__main__':
    # test_ex_2()
    pass