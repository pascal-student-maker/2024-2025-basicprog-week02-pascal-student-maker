def translate_month_number_to_str(month_number)->str:
   if (month_number == 1): return "January"
   elif(month_number == 2): return "February"
   elif(month_number == 3): return "March"
   elif(month_number == 4): return "April"
   elif(month_number == 5): return "May"
   elif(month_number == 6): return "June"
   elif(month_number == 7): return "July"
   elif(month_number == 8): return "August"
   elif(month_number == 9): return "September"
   elif(month_number == 10): return "October"
   elif(month_number == 11): return "November"
   elif(month_number == 12): return "December"
   else: return "Error message not a right month"
month_number = int(input("Enter a month number:  "))
print(f"  The corresponding month is: {translate_month_number_to_str(month_number)}")


          

  