# function with Outputs
'''
def my_function():
    result = 3*2
    return result

-> return value (in this case is result) will replace the line where function is called
'''

def format_name(f_name,l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    full_name = first_name + " " + last_name

    return f"{full_name}"

print(format_name('joNNY', 'DePP'))