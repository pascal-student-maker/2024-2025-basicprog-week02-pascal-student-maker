def assess_number(n):
    if (n>= 100):
        print("Wow, what a large number!")
        
def show_sum(number1, number2):
    total = number1 + number2
    print("Sum: " + str(total))   
    assess_number(total)     
    
def show_product(number1,number2):
    product = number1 * number2   
    print("Product:" + str(product))
    assess_number(product)
    
    
number1 = int(input("Enter the first number:"))   
number2 = int(input("Enter the second number:")) 
show_sum(number1,number2)
show_product(number1,number2)