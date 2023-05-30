# Prompt the user to enter the amount
amount = float(input("Please enter the amount: "))

# Check if the amount exceeds 1000
if amount > 1000:
    # If the amount exceeds 1000, calculate the discounted price
    discount = amount * 0.05
    discounted_price = amount - discount
    print("Discounted price:", discounted_price)
else:
    # If the amount is 1000 or less, no discount is applied
    print("No discount applied.")
