class My_dog:
    amount_of_years = 0
    def __init__(self, name = None , fur_color = None , weight = None, dog_breed = None):
        self.name = name
        self.height = 60
        self.dog_breed = dog_breed
        My_dog.amount_of_years += 1
        self.fur_color = fur_color
        self.weight = weight
    def __str__(self):
        return f'Woof! i`m a Dog, my name is {self.name}'

    def add_amount_of_years(self):
        self.amount_of_years += 5


print('-'*10, 'Steve', '-'*10, sep = '')
Steve = My_dog(name='Steve', fur_color='Gray',weight=36, dog_breed = 'Labrador Retriever')
Steve.add_amount_of_years()
print(Steve)
print(f'Steve is {Steve.amount_of_years} years old')
print(f'Steve`s fur color is {Steve.fur_color}')
print(f'Steve`s weight - {Steve.weight} kg')
Steve.height = 62
print(f'height Steve - {Steve.height} cm')
print(f'Steve`s breed is {Steve.dog_breed}')


print('-'*10, 'Bill', '-'*10, sep = '')
Bill = My_dog(name='Bill', fur_color='Dark grey',weight=40,  dog_breed = 'German Shepherd')
Bill.add_amount_of_years()
Bill.add_amount_of_years()
print(Bill)
print(f'Bill is {Bill.amount_of_years} years old')
print(f'Bill`s fur color is {Bill.fur_color}')
print(f'Bill`s weight - {Bill.weight} kg')
Bill.height = 65
print(f'height Bill - {Bill.height} cm')
print(f'Bill`s breed is {Bill.dog_breed}')
