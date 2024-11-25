a_pair_of_trousers = 70.5
a_t_shirt = 20.89
a_vest = 100.3

def total_amount_pay(trousers, t_shirts, vests):
    total_cost = trousers * a_pair_of_trousers + t_shirts * a_t_shirt + vests * a_vest
    return total_cost

a = int(input("How many trousers did you buy?: "))
b = int(input("How many t-shirts did you buy?: "))
c = int(input("How many vests did you buy?: "))

total_amount = total_amount_pay(a, b, c)
print(f"The total amount to pay is: {total_amount:.2f}")