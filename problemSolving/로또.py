from random import randint
numbers = set()
my_numbers = set()

while len(numbers) < 6:
    numbers.add(randint(1,45))
while len(my_numbers) < 6:
    my_numbers.add(randint(1,45))
    
print(f'금주 번호: {list(numbers)}', f'나의 번호: {list(my_numbers)}', sep = '\n')
