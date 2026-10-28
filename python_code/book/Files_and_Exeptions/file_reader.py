"""
Reading from a File
- reading an entire file
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()                       # read() returns an empty string when it reaches the end of the file
    print(contents.rstrip())                            # by using rstrip() we can remove the extra new line at the end of the file


# file path
# file_path = '/Users/username/Documents/pi_digits.txt'

# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())


"""
- reading line by line
"""

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)                                     # blank line appears because of print() function which adds a new line after each line is printed
        #print(line.rstrip())                           # by using rstrip() we can remove the extra new line at the end of each line

"""
-making a list of lines from a file
"""
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()                     # readlines() takes each line from the file and stores it in a list

for line in lines:
    print(line.rstrip()) 
