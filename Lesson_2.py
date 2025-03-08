class Student:
    amount_of_student = 0
    print('Hi')
    def __init__(self, name = None, scholarship = 50):
        self.name = name
        self.height = 170
        print('I am alive')
        Student.amount_of_student += 1
        self.scholarship = scholarship
    def __str__(self):
        return f'i`m a Student, my name is {self.name}'

    def add_scholarship(self):
        self.scholarship += 100

    def __del__(self):
        print(f'The student {self.name} is no longer enrolled at the university.')

print('-'*10, 'Tom', '-'*10, sep = '')
Tom = Student(scholarship = 100)
Tom.add_scholarship()
print(Tom.amount_of_student)
print(f'scholarship Tom - {Tom.scholarship}')
print(Tom)

print('-'*10, 'Bill', '-'*10, sep = '')
Bill = Student()
print(Bill.amount_of_student)
print(f'scholarship bill - {Bill.scholarship}')
print(Bill)

print()
print()
print()
print()
print(f'height Tom - {Tom.height}')
print(f'height Bill - {Bill.height}')
Tom.height = 180
print('-'*30)
print(f'height Tom - {Tom.height}')
print(f'height Bill - {Bill.height}')