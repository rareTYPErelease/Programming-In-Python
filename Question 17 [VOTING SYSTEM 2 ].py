#prompts user to input their citizenship:
citizenship=input("Please enter your citizenship:")

#options of citizenship available:
citizenship_options=["kenyan", "ugandan", "tanzanian"]

if citizenship.lower() in citizenship_options:
    age=int(input("Please enter your current age:"))
    
    if age>=18:
        print("you are eligible to vote.")
#when conditions required are met, the user is allowed voting:
        
    else:
        print("you are not eligible to vote.")
        
else:
    print("you are not eligble to vote or a citizen.")
#if one or none of the requirements are met, the use is denied voting:
