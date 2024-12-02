def give_fahrenheit(t_in_celsius: float) -> float:
    return (t_in_celsius * 9 / 5) + 32  # Perform arithmetic with float

def give_celcius(t_in_fahrenheit: float) -> float:
    return (t_in_fahrenheit - 32) * 5 / 9  # Perform arithmetic with float

# Ask the user to choose a temperature unit
unit = input("Which temperature unit do you want to convert? [C: Celsius, F: Fahrenheit]: ").strip().upper()

if unit == 'C':
    # Get temperature in Fahrenheit and convert it to Celsius
    t_in_fahrenheit = float(input("Enter a temperature in Fahrenheit: "))  # Convert input to float
    print(f"The corresponding temperature in Celsius is: {give_celcius(t_in_fahrenheit)}°C")
elif unit == 'F':
    # Get temperature in Celsius and convert it to Fahrenheit
    t_in_celsius = float(input("Enter a temperature in Celsius: "))  # Convert input to float
    print(f"The corresponding temperature in Fahrenheit is: {give_fahrenheit(t_in_celsius)}°F")
else:
    print("Invalid input! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
