# Prompt the user to enter their age and citizenship
age = int(input("Please enter your age: "))
citizenship = input("Please enter your citizenship (KENYAN, UGANDAN, or TANZANIAN): ")

# Check if the person meets the criteria for voting
if age >= 18 and citizenship in ["Kenyan", "Ugandan", "Tanzanian"]:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
