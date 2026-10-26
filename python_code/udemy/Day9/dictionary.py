# {key:value}
# {key:value, key:value}

programming_dictionary = {
    'Bug':'A bug is a defect or error in a computer program that causes it to produce an unexpected or wrong result',
    'Function':'A function is a self-contained block of reusable code that takes inputs, performs a specific task, and can return an output',
    }

print(programming_dictionary['Bug'])
programming_dictionary['Loop'] = 'The action of doing something over and over again'
print(programming_dictionary)


# wipe and existing dictionary
# programming_dictionary = {}


# Edit an item in a dictionary
programming_dictionary['Bug'] = 'A moth in your computer'
print(programming_dictionary)


# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
