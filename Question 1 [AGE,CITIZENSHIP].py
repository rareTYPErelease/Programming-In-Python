# Prompt user for their citizenship and age
citizenship = input("Are you a Kenyan citizen? (yes/no): ")
age = int(input("Enter your age: "))

# Check eligibility based on citizenship and age
if citizenship == "yes" and age >=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

