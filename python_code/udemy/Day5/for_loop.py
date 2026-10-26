fruits = ["Apple", "Banana","Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")


# find a max number from list

# 1. max built in function

# 2. make max logic by myself

student_scores = [180,124,165,173,189,169,146]

max = 0
for score in student_scores:
    if score > max:
        max = score
    else:
        continue

print(f"Max score is {max}")