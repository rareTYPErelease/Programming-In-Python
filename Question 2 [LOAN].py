# Prompt the user to enter their age
age = int(input("Please enter your age: "))

# Prompt the user to enter their annual income
income = float(input("Please enter your annual income: "))

# Check the age and income
if age >= 21 and income >= 21000:
    print("Congratulations! You qualify for a loan.")
else:
    print("Unfortunately, you don't qualify for a loan.")
