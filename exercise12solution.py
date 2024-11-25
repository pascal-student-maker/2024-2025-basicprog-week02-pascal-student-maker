def translate_month_number_to_str(month_number):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December" 
    }

    if month_number in months:
        return months[month_number]
    else:
        return "Invalid month number"

month_number = int(input("Enter a month number: "))
month_name = translate_month_number_to_str(month_number)
print(month_name)