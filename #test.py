#test.py


a_pair_of_trousers = 70.5
a_t_shirt = 20.89
a_vest = 100.3
print("***Welcome to the checkout system***.")
a= int(input("How many trousers did you buy?:"))
b= int(input("How many t-shirts did you buy?:"))
c= int(input("How many vest did you buy?:"))

def total_amount_pay(a_pair_of_trousers ,a_t_shirt,a_vest ):
    total =  a_pair_of_trousers *a + a_t_shirt*b+ a_vest*c
    print(f" The total amount to pay is : {total:.2f}")
    
total_amount_pay(a_pair_of_trousers,a_t_shirt,a_vest)    
