#exercise 4c



def show_message(current_hour,firstname:str) -> str:
    if ((current_hour >= 7) and ( current_hour < 12 )):
        return(f" Good morning {firstname}  " )
    elif (( current_hour >= 12) and ( current_hour <= 13)):
        return(f" Yay it's afternoon {firstname}")   
    elif((current_hour >= 13)  and (current_hour <= 17)):
        return(f" Good afternoon {firstname}")
    elif((current_hour >= 17) and (current_hour<= 21)):
        return(f"Good evening {firstname}")
    elif((current_hour >= 21) or (current_hour<= 7)):
        return(f"Good night {firstname}")
    else:
        return(" No clue what time it is")     

import datetime
now = datetime.datetime.now()                
current_hour = now.hour
firstname = input("What is your first name?")
welcome = show_message(current_hour, firstname)
print(welcome)