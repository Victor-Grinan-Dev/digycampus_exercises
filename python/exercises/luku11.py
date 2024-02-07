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

"""
TASK:

Write a class HybridCar that inherits both the Car and ElectricCar classes. (In this order).
Override the calculate_range(self) method of the superclassess so that it calculates the sum of the values returned by the same-named methods of both superclassess.
Override the drive(self, distance) method of the superclassess so that:
First, check if the combined range (battery and fuel) is sufficient. If not, print the following message, where X is the combined range rounded to two decimal places:
'Cannot travel that distance, current range: X km'
If the range is sufficient, consume the battery first and then the fuel using the methods drive() and calculate_range() of the superclassess. Essentially, drive first with the ElectricCar class, and if the battery runs out, continue with the Car class.

Override the status(self) method of the superclassess so that it returns a string "X Y", where X is the return of the status method of the ElectricCar class, and Y is the return of the status method of the Car class. (note the space!)
TIPS:

When inheriting multiple classes, you can access the method of the desired superclass as follows: ElectricCar.drive(self, 5) In addition to the traveled distance, provide self as an argument that directs the method call to the superclass ElectricCar.
"""
#ex.4
class Car:
    def __init__(self, fuel_consumption):
        self.traveled_distance = 0
        self.fuel = 50
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel - self.fuel_consumption * distance >= 0:
            self.traveled_distance += distance
            self.fuel -= self.fuel_consumption * distance
            print('using', round(self.fuel_consumption*distance, 2), 'liters of fuel to drive', round(distance, 2), 'km')

        else:
            return False

    def refuel(self, fuel_amount):
        self.fuel = min(self.fuel + fuel_amount, 50)

    def calculate_range(self):
        return self.fuel / self.fuel_consumption

    def status(self):
        fuel = str(round(self.fuel, 2))
        return 'Remaining fuel ' + fuel + ' liters'


class ElectricCar:
    def __init__(self, battery_consumption):
        self.battery = 100
        self.battery_consumption = battery_consumption
        self.traveled_distance=0

    def drive(self, distance):
        if self.battery - self.battery_consumption * distance >= 0:
            self.traveled_distance += distance
            self.battery -= self.battery_consumption * distance
            print('using', round(self.battery_consumption*distance, 2), '% battery to drive', round(distance,2), 'km')
        else:
            return False

    def charge_battery(self, charge):
        self.battery = min(self.battery + charge, 100)

    def calculate_range(self):
        return self.battery / self.battery_consumption

    def status(self):
        btr = str(round(self.battery, 2))
        return 'Remaining battery ' + btr + '%'
"""
In Python, a class can inherit properties from multiple superclassess. Familiarize yourself with the topic online and then proceed with the task below:

TASK:

1- Write a class HybridCar that inherits both the Car and ElectricCar classes. (In this order).

2- Override the calculate_range(self) method of the superclassess so that it calculates the sum of the values returned by the same-named methods of both superclassess.

3- Override the drive(self, distance) method of the superclassess so that:
First, check if the combined range (battery and fuel) is sufficient. If not, print the following message, where X is the combined range rounded to two decimal places:
'Cannot travel that distance, current range: X km'
If the range is sufficient, consume the battery first and then the fuel using the methods drive() and calculate_range() of the superclassess. Essentially, drive first with the ElectricCar class, and if the battery runs out, continue with the Car class.

4- Override the status(self) method of the superclassess so that it returns a string "X Y", where X is the return of the status method of the ElectricCar class, and Y is the return of the status method of the Car class. (note the space!)
TIPS:

When inheriting multiple classes, you can access the method of the desired superclass as follows: ElectricCar.drive(self, 5) In addition to the traveled distance, provide self as an argument that directs the method call to the superclass ElectricCar.
"""

class HybridCar(Car, ElectricCar):
    def __init__(self, fuel_consumption, battery_consumption):
        Car.__init__(self, fuel_consumption) 
        ElectricCar.__init__(self, battery_consumption)
    
    def calculate_range(self):
        return self.battery / self.battery_consumption + self.fuel / self.fuel_consumption
    
    def max_battery_yield(self, battery_status):
        return round(battery_status / self.battery_consumption)  

    def drive_with_battery(self, distance):
            self.traveled_distance += distance
            self.battery -= self.battery_consumption * distance
            print('using', round(self.battery_consumption*distance,1), '% battery to drive', round(distance,2), 'km')

    def drive_with_fuel(self, distance):
            self.traveled_distance += distance
            self.fuel -= self.fuel_consumption * distance
            print('using', round(self.fuel_consumption*distance, 1), 'liters of fuel to drive', round(distance, 2), 'km')

    def drive(self, distance):
        range = self.calculate_range()
        max_distance_with_battery= self.max_battery_yield(self.battery)
        self.traveled_distance = 0
        if range > distance:
            if distance <= max_distance_with_battery:
                self.drive_with_battery(distance)

            elif distance > max_distance_with_battery:
                self.drive_with_battery(max_distance_with_battery)
                distance-= max_distance_with_battery
                self.drive_with_fuel(distance)

        else:
            print(f'Cannot travel that distance, current range: {round(range,2)} km')
            return f'Cannot travel that distance, current range: {round(range,2)} km'

    def status(self):
        return f'{ElectricCar.status(self)} {Car.status(self)}'

def test_ex_4():

    # auto = HybridCar(0.05, 0.7)
    # auto.status()
    # auto.drive(50)
    print('HybridCar is a subclass of Car'
        if Car in type.mro(HybridCar) else
        'HybridCar is not a subclass of Car!!')

    print('HybridCar is a subclass of ElectricCar'
        if ElectricCar in type.mro(HybridCar) else
        'HybridCar is not a subclass of ElectricCar!!')

    auto = HybridCar(0.05, 0.7)
    auto.drive(20)
    auto.drive(100)
    auto.drive(50)
    print(auto.status())
    auto.charge_battery(100)
    auto.refuel(100)
    print(auto.status())
    auto.drive(1000)

    print('**********************************')

    # auto = HybridCar(0.05, 0.7)
    # auto.drive(1000)
    # print(auto.status())
    # auto.drive(1000)

if __name__ == '__main__':
    # test_ex_2()
    # test_ex_3()
    test_ex_4()
    pass