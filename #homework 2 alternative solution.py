#homework 2 alternative solution 

 
def exclusive_include( a,b):
    result = a * b
    print(f" the result is the amount including vat,: {result}")
    return result
    
a = 180000
b = 1.21 
result = exclusive_include(a, b)   
result = result + 10
print(result)