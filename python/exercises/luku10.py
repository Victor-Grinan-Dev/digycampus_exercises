import random

class MyEmployee:
   
    days_since_raise = 0
    __salary = 2000
    __total_hours = 0

    def __init__(self, name):
        self.name = name

    def complete_workday(self, hours):
        self.__total_hours += hours
        # self.__hours += hours 
        # days = self.__hours // 6
        # if self.__hours % 6 > 0:
        #     self.__hours = self.__hours % 6
        #     self.days_since_raise += days
        if hours > 6:
            self.days_since_raise += 1
    
    def eligible_for_raise(self):
        return self.days_since_raise > 365 
    
    def give_raise(self, percentage_increase):
        self.__salary += self.salary * (percentage_increase/100)
        self.days_since_raise = 0
        
    @property
    def salary(self):
        return round(self.__salary, 1)
    
    @property
    def hours(self):
        return self.__total_hours

class Employee:
   
    days_since_raise = 0
    salary = 2000
    hours = 0

    def __init__(self, name):
        self.name = name

    def complete_workday(self, hours):
        self.hours += hours
        if hours > 6:
            self.days_since_raise += 1
    
    def eligible_for_raise(self):
        return self.days_since_raise > 365
    
    def give_raise(self, percentage_increase):
        self.salary += self.salary * (percentage_increase/100)
        self.days_since_raise = 0 

def test_ex_1():
    print("Testatan luokan koko toimintokirjoa!")
    Jani = Employee("Jani")
    Simo = Employee("Simo")
    Tiina = Employee("Tiina")
    Elli = Employee("Elli")

    list_employees = [Jani, Simo, Tiina, Elli]
    # list_employees = [Jani]

    for day in range(365 * 4):
        for employee in list_employees:
            add_hours = random.randint(2, 16)
            # print('add hour:', add_hours)
            employee.complete_workday(add_hours)
            if employee.eligible_for_raise():
                print("Day:", day)
                print(employee.name, "is eligible for a raise, after having worked for", employee.hours, "hours!")
                employee.give_raise(5)
                print("His/Her salary is now : ", employee.salary, "(+{}%)".format(5))
                

def test_ex_1_once():
    Jani = Employee("Jani")
    Jani.complete_workday(3000) 
    Jani.give_raise(5)
    print(Jani.salary)


if __name__ == '__main__':
    test_ex_1()
    # test_ex_1_once()