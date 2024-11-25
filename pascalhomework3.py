#homework 3
import datetime
now = datetime.datetime.now()
def show_message():

    now = datetime.datetime.now()
    hour = now.hour  
    if hour in (7, 12):
        print("Good morning, Charles")
    
    elif hour in (12,13):
        print("yay its afternoon Charles")
    elif hour in (13,17):
        print("Good afternoon charles")  
    elif hour in (17,21):
        print("good evening charles") 
    elif hour in (21,7):   
         print("Good night charles")     
# Example usage
hour = int(input("What time is it : "))
firstname = input("What is your first name?")
welcome = show_message(hour, firstname)
print(welcome)