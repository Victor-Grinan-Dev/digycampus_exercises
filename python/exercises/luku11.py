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