print("Welcome to the treasure Island")
print("================================")
print("Your Mission: Find a treausre")

answer = input("Which way you want to go? (left / right)\n").lower()

if answer == "left":
    answer1 = input("Do you want to wait or swim\n").lower()
    if answer1 == "wait":
        answer2 = input("Which door you want to open(blue/yellow/red)\n").lower()
        if answer2 == "yellow":
            print("You win!! Congratulations you found a treasure")
        else:
            print("Game over. You couldn't find a treausre")
    else:
        print("Game over. You couldn't find a treausre")
else:                
    print("Game over. You couldn't find a treausre")



