#homework2b
excl_VAT = float(input("What is the amount excluding VAT?"))
VAT_percentage = float(input("What is the percentage of VAT?"))
def exclusive_to_include(excl_VAT:int, VAT_percentage:float) -> float:
    incl_VAT = (excl_VAT * VAT_percentage)
    return incl_VAT
incl_VAT = exclusive_to_include(200,1.21)
print(f" the inclusive amount you have to pay is   : {incl_VAT}")

 


