import random

people_list = ["Kevin","Angelica", "Josh","Jayson","Kara"]

# 1. Option
# use built in function
select_person = print(random.choice(people_list))

# 2. Option
# generate random number and use it as index number of list
random_index = random.randint(0,4)
print(people_list[random_index])