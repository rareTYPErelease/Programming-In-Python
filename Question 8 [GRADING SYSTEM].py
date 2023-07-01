maths = int (input("Input Maths marks"))
eng = int (input("Input english marks"))
swa = int (input("Input swahili marks"))

if maths <0 or maths>100 or eng<0 or eng>100 or swa<0 or swa>100 :
    print("Invalid marks entered")

else:
    marks=(maths+eng+swa)/3
    print("your average is ",marks)
    
if marks > 70 :
 print("Grade: A")
elif marks >= 60 and marks < 69:
 print("Grade: B")
elif marks >= 50 and marks < 59:
 print("Grade: C")
elif marks >= 40 and marks < 49:
 print("Grade: D")
else:
 print("Failed exam")
