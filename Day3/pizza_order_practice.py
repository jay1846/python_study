print("Welcom to python Pizza Delivery")

size = input("What size do you want? (S/M/L)")
pepperoni = input("Do you want pepperoni on top? (y/n)")
extra_cheese = input("Do you want extra cheese on top? (y/n)")
bill = 0

if size == "S":
    bill += 15
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1

elif size == "M":
    bill += 20
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1

else:
    bill += 25
    if pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1


print(f"Your {size}pizza costs ${bill}")