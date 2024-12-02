#homework 3c

def show_message(hour:int,firstname:str) -> str:
    if ((hour >= 7) and ( hour < 12 )):
        print(f" Good morning {firstname}  " )
    elif (( hour >= 12) and ( hour <= 13)):
        print(f" Yay it's afternoon {firstname}")   
    elif((hour >= 13)  and (hour <= 17)):
        print(f" Good afternoon {firstname}")
    elif((hour >= 17) and (hour<= 21)):
        print(f"Good evening {firstname}")
    elif((hour >= 21) or (hour<= 7)):
        print(f"Good night {firstname}")
    else:
        print(" No clue what time it is")               
hour = int(input("What time is it?"))
firstname = input("What is your first name?")
welcome = show_message(hour, firstname)
print(welcome)