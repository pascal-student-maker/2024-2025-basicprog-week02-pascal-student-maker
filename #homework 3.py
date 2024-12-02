#homework 3
def def_show_message(time_range):
    if time_range == (7, 12):  # 7:00 to 12:00
        print("Good Morning!")
    elif time_range == (12, 13):  # 12:00 to 12:59
        print("It's Noon!")
    elif time_range == (13, 17):  # 13:00 to 16:59
        print("Good Afternoon!")
    elif time_range == (17, 21):  # 17:00 to 20:59
        print("Good Evening!")
    elif time_range == (21, 7):  # 21:00 to 6:59 (spanning to next day)
        print("Good Night!")
    else:
        print("Invalid time range")

hxour = int(input("what time is it ?"))
firstname = input(" What is your first name ?")
welcome = def_show_message(hour ,firstname)