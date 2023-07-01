#ask the user to guess the number
guess = int(input("Guess the number: "))

#Compare the guess with the target number
if guess == 300:
    print("Congratulations! You guessed the correct number!")
   
elif guess < 300:
    print("Too low! Try guessing a higher number.")
else:
    print("Too high! Try guessing a lower number.")
