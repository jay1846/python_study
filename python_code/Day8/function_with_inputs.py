# Functions with Inputs
# def my_function(something):
#     #do this with something

def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?\n")

greet()

def greet_with_name(name):
     print(f"Hello {name}")
     print(f"How do you do {name}?")
     print("Isn't the weather nice?\n")

greet_with_name("Jay")


# Positional & Keyword parameters
def greet_with(name,location):
     print(f"Hello {name}")
     print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")

# we don't want this result
greet_with("Nowhere", "Jack Bauer")

# instead we can do
greet_with(location="Nowhere", name="Jack Bauer")