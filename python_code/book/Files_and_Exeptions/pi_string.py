'''
Working with a file's contents
    - after we've read a file into memory, we can do whatever we want with data
'''
filename = 'pi_digits.txt'

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()                  # by using strip() we could erase left side of blank

print(pi_string)
print(len(pi_string))


'''
Large files: one million digits
'''
filename2 = 'pi_million_digits.txt'
with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string2 = ''
for line in lines:
    pi_string2 += line

print(pi_string2[:52] + '...')                     # pi_string2[:52] -> from 0 to 51
print(len(pi_string2))


'''
Check if my birthday is contained in Pi
'''
filename2 = 'pi_million_digits.txt'
with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string2 = ''
for line in lines:
    pi_string2 += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string2:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear :/")
