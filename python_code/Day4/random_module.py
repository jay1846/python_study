# how to import modules
import random

# my own module
import my_number

# access functions of module by using .
random_integer = random.randint(1,10)
print(random_integer)

# access value by using dot
print(my_number.my_favorite_number)

# random floating number range 0 to 1
random_0_to_1 = random.random()
print(random_0_to_1)

random_float = random.uniform(1,10)
print(random_float)

random_head_or_tail = random.randint(0,1)
if random_head_or_tail == 0:
    print("head")
else:
    print("tail")