import random
bigdata = []
for i in range(100):
    bigdata.append(random.randint(1,33))
numbers = set(i for i in range(1,34))
nodata = list(numbers - set(bigdata))
print(nodata)
