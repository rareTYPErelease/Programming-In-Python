#user input
salary=float (input("kindly input your salary for this month"))
years=int (input ("Kindly input the number of years you have worked"))

if years >= 10:
    bonus = 0.01 * salary
    print(bonus)
if years <= 10:
    bonus = 0.08 * salary
    print(bonus)
else:
    bonus2 = 0.05*salary 
    print(bonus2)

else:
    print("Invalid input. Please enter positive values for salary and years worked.")
