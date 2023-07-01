def get_even_numbers(numbers):
   
    even_numbers = []  #list to store even numbers
    
    for number in numbers:
        if number % 2 == 0:  # Check if the number is even by dividing it by 2 and checking for a remainder of 0
            even_numbers.append(number)  
    
    return even_numbers  # Return the list of even numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # List of numbers to be filtered
even_numbers = get_even_numbers(numbers)  
print(even_numbers)  
