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

#ex.3
class Product:

    def __init__(self, product_id, title, price):
        self.id = product_id
        self.title = title
        self.price = price
        self.original_price = price
    
    def put_on_sale(self, discount_percentage ):
        self.price -= self.price * ( discount_percentage * 0.01 )

    def return_to_normal_price(self):
        self.price = self.original_price

class Printer(Product):
    def __init__(self, product_id, title, price, manufacturer, model):
        Product.__init__(self, product_id, title, price)
        self.manufacturer = manufacturer
        self.model = model

    def print(self, text):
        print('======', self.manufacturer, self.model, '======')
        print('<', text, '>')


class Book(Product):
    def __init__(self, product_id, title, price, publisher, isbn):
        super().__init__(product_id, title, price)
        self.publisher = publisher
        self.isbn = isbn

"""
1-Write a class Textbook that inherits the given class Book, which has an additional public attribute course_id.

2- Extend the superclass Product so that it includes methods
put_on_sale, which reduces the product's price (attribute price) based on the given argument discount_percentage (integer).

3- return_to_normal_price, which restores the product's price to its original value.

4- Modify the Textbook class so that it overrides the superclass method put_on_sale. The put_on_sale method of the Textbook class reduces the price by only half of the given percentage. That is, a.put_on_sale(10), where a is an instance of the Textbook class, reduces the price by only 5 percent.
"""

class Textbook(Book):

    def __init__(self, product_id, title, price, publisher, isbn, course_id):
        super().__init__(product_id, title, price, publisher, isbn)
        self.course_id = course_id 
        
    def put_on_sale(self, discount_percentage ):
        self.price -= self.price * (( discount_percentage * 0.01 ) / 2)


def test_ex_3():
    tuotteet = [
    Book(1, 'Old Man and the Sea', 25, 'Penguin Publishing', '0684801221'),
    Textbook(2, 'Space Flight Dynamics', 55, 'Wiley', '978-1-119-15782-3', 'PHYSICS-255'),
    Printer(15, 'Pixma Colormax', 155, 'Canon', '3500')
    ] 
    print('Alennetaan aluksi hintaa 15%')
    for t in tuotteet:
        t.put_on_sale(15)
        print('Product:', t.id, t.title, 'on sale (15%)')
        print('Discount from original price:', t.original_price, '->', t.price,
            'change:', round((t.price/t.original_price-1)*100, 2), '%')
        
    print('Alennetaan vielä hintaa 20%')
    for t in tuotteet:
        t.put_on_sale(20)
        print('Product:', t.id, t.title, 'on sale (20%)')
        print('Discount from original price:', t.original_price, '->', t.price,
            'change:', round((t.price/t.original_price-1)*100, 2), '%')
        
    print('Palautetaan lopulta hinnat takaisin alkuperäisiksi')
    for t in tuotteet:
        t.return_to_normal_price()
        print('Product:', t.id, t.title, 'returns to original price :', t.price)

if __name__ == '__main__':
    # test_ex_2()
    test_ex_3()
    pass