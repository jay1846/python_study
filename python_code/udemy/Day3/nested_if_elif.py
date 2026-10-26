print("Welcome to roller coaster")

height = int (input("What is your height in cm? "))

if height > 120:        # greater than/ does not include 120
                        # >= greater than and equal to
    print("You can ride the rollercoaster\n")
    age = int(input("How old you are? "))
    if age <=18:
        print("Please pay $10\n")
    elif 12 <= age <18:
        print("Please pay $7\n")
    else:
        print("Please pay $5\n")
else:
    print("Sorry you have to grow up more :/\n")
