print("Welcome to roller coaster")

height = int (input("What is your height in cm? "))
bill = 0
if height > 120:        # greater than/ does not include 120
                        # >= greater than and equal to
    print("You can ride the rollercoaster\n")
    age = int(input("How old you are? "))
    if age >= 18:
        print("Please pay $10\n")
        bill = 10
    elif 12 <= age <18:
        print("Please pay $7\n")
        bill = 7
    else:
        print("Please pay $5\n")
        bill = 5

    wants_photo = input("Do you want to have a photo (y/n)")
    if wants_photo == "y":
        bill += 3
    
    print(f"Your final bill is ${bill}")


else:
    print("Sorry you have to grow up more :/\n")
