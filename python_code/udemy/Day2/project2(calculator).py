print("welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip do you want to give (10/12/15): "))
divide_people = int(input("How many people to split the bill? "))

total_bill = (bill * (tip/100)) + bill
each_bill = total_bill / divide_people
final_amount = around(each_bill,2)
print(f"Each person should pay {final_amount}")