#exercise 1
#a = (int(input(" What is the first number?")))
#b = (int(input("What is the second number?")))
#if a == b:
   # print("the numbers are the same")
#else: 
   # print("the numbers are different")
    
#exercise 2
#a = (int(input("Give an integer:")))
#if a %2 == 0:
   # print("The number is even ")
#else:print("The Provided number is odd")

#exercise 3
#a = int(input("What is your year of birth?:"))   
#b = int(input("What month were you born?:"))
#if a >= 2006 and b >= 11:
   # print(" You are under 18, so you cannot drink alcohol")
#else:
    #print(" You are over 18 so you are allowed to drink beer")    
    
 #exercise 3 solution
 
#import datetime

#current_year = datetime.datetime.now().year
#a = int(input("What is your year of birth?:"))
# = int(input("What month were you born?:"))

#if current_year - a > 18 or (current_year - a == 18 and b <= 10):
   # print("You are over 18 so you are allowed to drink beer")
#else:
    #print("You are under 18, so you cannot drink alcohol")
    
#exercise 4
#def human_years(dog_age):
   # if dog_age == 0:
    # print("error message")   
    #if dog_age == 1:
     #   print("14 human years")
    #if dog_age == 2:
     #   print(" 22 human years")   
    #if dog_age >= 2:
    # return 22 + (dog_age-2)*5 
#dog_age = int(input(" Enter  the age of the dog in dog years:")) 
#human_age = human_years(dog_age)
#print(f"A {dog_age}- year old human is equivalent to a {human_age} year old doge in terms of age.")

# exercise 5
#a = (float(input(" Enter your score:"))) 

#if round (a) >= 10:
   # print (" Congratulations, you passed !")
#else:
 #print (" Alas, better luck next time")
  
#exercise 6
#str(input("Enter a first word:"))
#str(input("Enter a second word:"))

#exercise 7
#a = str(print(" Howest"))
#b = str(print("hOwEst"))
#if a ==b:
  # print(" The words Howest and hOwest are identical.")
#else:
   # print(" The words Howest and hOwest are not indentical.")

#exercise 08
#def print_welcome(name ):
   #print (f"Welcome {name} what is your name")   
   #print_welcome(name = "Joerie") 
   #print_welcome("Joerie")
   
#exercise 09
#def create_welcome_in_class (name, classgroup="1CTAI1" "1MCT1"):
 #print(f" Welcome  {name} from {classgroup} at Howest")  
 #print(f" What is your first name ? {name}")  
 #print(f" what is your classgroup {classgroup}") 
 #print(f"Welcome Joerie in {classgroup}")
#name = "Joerie"
#classgroup = "1CTAI1"
#create_welcome_in_class(name,classgroup)

#exercise 10
#def equation ( a= 0 , b= 0 ,c = 0 , d= 0):
   # result =  a -b + c - d
   # print(f"{a} - {b} + {c} - {d} =  {result}")
   # return result
    
#a = 5
#b = -4
#c = 0
#d = 0
#equation (a,b,c,d)
#result = equation(5,-4,0,0)
#print(f" the result is:", {result})

#equation 11
#def show_max  ( a= 0 , b = 0 , c = 0):
   # result = max
   # print(f"{a}, {b}, {c}")
   # return result
#a = 4
#b = 2
#c = 6
#show_max (a,b,c)
#result = max(4,2,6)
#print(f" the result is:", {result})

#exercisen 12
#def translate_month_number_str ( 1  January , 2 = February , 3 = March , 4 = April 5 = May, 6 = June):
   # result = 1,2,3,4,5,6
    #print(f"the result is:" ,{result})
    #return result
#1# = January
#2 #= February
#3 #= March 
#4 #= April   
#5 #= May
#6 =# June 
#translate_month_number_str ( 1, 2 ,3 ,4 ,5 6)
#result = January , February, March , April , May, June
#print(f" the result is:", {result})
#solution 12 
#def translate_month_number_str(month_number):
  #"""
  #This function translates a month number to its corresponding month name.

  #Args:
   #   month_number: An integer between 1 and 12 representing the month number.

  #Returns:
   #   The month name as a string (e.g., "January", "February", etc.) or None if the month number is invalid.
  #"""
 # month_names = {
   #   1: "January",
   #   2: "February",
    #  3: "March",
    #  4: "April",
    #  5: "May",
    #  6: "June",
    #  7: "July",
    #  8: "August",
    #  9: "September",
    #  10: "October",
    #  11: "November",
    #  12: "December"
  #}

  #if month_number in month_names:
   #   return month_names[month_number]
  #else:
  #    return None  # Return None for invalid month numbers

# Example usage
#month_number = 3
#month_name = translate_month_number_str(month_number)

#if month_name:
 ## print(f"The month name for {month_number} is: {month_name}")
#else:
 # print(f"Invalid month number: {month_number}")

 #exercise 13
def give_celsius = int(input("receives  a temperature in fahrenheit"))

#exercise 13 Solution 
def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  fahrenheit = (celsius * 9 / 5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius

# Get user input for temperature unit and value
temperature_unit = input("Which temperature unit do you use? [C: Celsius, F: Fahrenheit]: ").upper()
temperature_value = float(input("Enter a temperature in {}: ".format(temperature_unit)))

# Convert and print the result
if temperature_unit == "C":
  converted_temperature = celsius_to_fahrenheit(temperature_value)
  print(f"The corresponding temperature in Fahrenheit is: {converted_temperature:.2f}")
elif temperature_unit == "F":
  converted_temperature = fahrenheit_to_celsius(temperature_value)
  print(f"The corresponding temperature in Celsius is: {converted_temperature:.2f}")
else:
  print("Invalid temperature unit. Please enter 'C' or 'F'.")
   #homework 1
 
# Prices of items
A_Pair_of_Trousers = 70.5
A_T_shirt = 20.89
A_Vest = 100.3

# Input from the user
a = int(input("How many trousers have been bought?: "))
b = int(input("How many T-shirts have been bought?: "))
c = int(input("How many vests have been bought?: "))

# Calculate the total amount to pay
Total_Amount_To_Pay = (A_Pair_of_Trousers * a) + (A_T_shirt * b) + (A_Vest * c)

# Print the summary
print(f"""
*** Welcome to the checkout system *** 
How many trousers have been bought?: {a}
How many T-shirts have been bought?: {b}
How many vests have been bought?: {c}

You have bought:
    Trousers : {a} pair(s)
    T-shirts : {b} pair(s)
    Vests    : {c} piece(s)

The total amount to pay is: ${Total_Amount_To_Pay:.2f}
""")

# Define a function to calculate the total amount
def amount_to_pay(trousers_price, t_shirt_price, vest_price, trousers_qty, t_shirts_qty, vests_qty):
    result = (trousers_price * trousers_qty) + (t_shirt_price * t_shirts_qty) + (vest_price * vests_qty)
    print(f"""
    Calculation:
    {trousers_qty} trousers @ ${trousers_price:.2f} each = ${trousers_price * trousers_qty:.2f}
    {t_shirts_qty} T-shirts @ ${t_shirt_price:.2f} each = ${t_shirt_price * t_shirts_qty:.2f}
    {vests_qty} vests @ ${vest_price:.2f} each = ${vest_price * vests_qty:.2f}
    Total = ${result:.2f}
    """)
    return result

# Call the function
amount_to_pay(A_Pair_of_Trousers, A_T_shirt, A_Vest, a, b, c)
 #homework 2
def exclusive_include( a,b):
    result = a * b
    print(f" the result is the amount including vat,: {result}")
    return result 
a = 180000
b = 1.21 
exclusive_include (a,b)
result = exclusive_include(a * b)   
print(f"The result is the amount including VAT: {result}")


