print("welcome to the tip calculator")
bill = input("What was the total bill? ")
tip = input("How much tip do you want to give (10/12/15): ")
divide_people = input("How many people to split the bill? ")

total_bill = float(bill)*float(int(tip)/100) + float(bill)
each_bill = total_bill / int(divide_people)
print("each people should pay: " + str(round(each_bill,2)))