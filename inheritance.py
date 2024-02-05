class Employee:
    raise_amt =1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


employee1 = Employee('Juan', 'Pachanga', 700)
dev_1 = Developer('Victor', 'Grinan', 700, 'Python')
dev_2 = Developer('Jorge', 'Machete', 700, 'Java')
mgr_1 = Manager('Sue', 'Smith', 1000, [dev_1])

def print_help():
    print(help(employee1))
    print(help(dev_1))

def print_separator(title):
    print()
    print('*******************')
    if title:
        print(f"{title}:")
    print()

def print_apply_raise():
    print(employee1.pay)
    employee1.apply_raise()
    print(employee1.pay)
    print_separator()
    print(dev_1.pay)
    dev_1.apply_raise()
    print(dev_1.pay)
 
def print_developer_email():
    print(dev_1.email())
    print(dev_1.prog_lang)

def print_isinstance(child, parent):
    print(isinstance(child, parent))

def print_issubclass(child, parent):
    print(issubclass(child, parent))


if __name__ == "__main__":
    # print_help()
    # print_apply_raise()
    mgr_1.add_emp(dev_2)
    print(mgr_1.email())
    mgr_1.print_emp()

    print_separator('IS INSTANCE')
    print_isinstance(mgr_1, Employee)
    print_isinstance(mgr_1, Developer)
    print_isinstance(dev_1, Employee)
    print_separator('IS SUBCLASS')
    print_issubclass(Manager, Employee)
    print_issubclass(Developer, Employee)
    print_issubclass(Developer, Manager)