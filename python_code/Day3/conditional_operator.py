print("Wlcome to Rollercoaster")

height = int (input("What is your height in cm? "))

if height > 120:        # greater than/ does not include 120
                        # >= greater than and equal to
    print("You can ride the rollercoaster\n")
else:
    print("Sorry you have to grow up more :/\n")


# Modulo Operator ( % )
print(10%3)     # --> show remainder

number = int(input("Enter number that you want to check: "))

if (number % 2 == 0):
    print(f"{number} is even\n")
else:
    print(f"{number} is odd number\n")