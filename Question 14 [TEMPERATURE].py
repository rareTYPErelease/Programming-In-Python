# User input for temperature values

celsius_input = float(input("Enter the temperature in Celsius: "))
fahrenheit_input = float(input("Enter the temperature in Fahrenheit: "))

class Temperature:
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    
    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")

# Instance of the Temperature class
temp = Temperature()

temp.convertFahrenheit(celsius_input)# Convert Celsius to Fahrenheit
temp.convertCelsius(fahrenheit_input)# Convert Fahrenheit to Celsius
