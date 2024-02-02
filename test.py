class Test:
    def __init__(self, name):
        self.name = name
    
    def change_name(self, new_name):
        self.name = new_name


new_test = Test('Victor')
new_test.change_name('Roberto')
print(new_test.name)

new_test = Test(2000)
new_test.change_name(2100)
print(new_test.name)