def exclusive_to_include(excl_Vat: float, vat_percentage: float) -> float:
    # Calculate VAT-inclusive amount
    incl_Vat = excl_Vat + (excl_Vat * vat_percentage / 100)
    return incl_Vat

# Input values
excl_VAT = float(input("What's the amount excluding VAT? "))
vat_percentage = float(input("What's the percentage of VAT? "))

# Calculate VAT-inclusive amount
incl_VAT = exclusive_to_include(excl_VAT, vat_percentage)

# Output the result
print(f"The amount including VAT is: {incl_VAT}")
