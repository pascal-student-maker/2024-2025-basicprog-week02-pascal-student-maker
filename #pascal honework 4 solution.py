#pascal homework 4 solution 
import datetime

def show_message(hour: int, firstname: str) -> str:
    if 7 <= hour < 12:
        return f"Good morning, {firstname}"
    elif 12 <= hour < 13:
        return f"Yay, it's afternoon, {firstname}!"
    elif 13 <= hour < 17:
        return f"Good afternoon, {firstname}"
    elif 17 <= hour < 21:
        return f"Good evening, {firstname}"
    else:  # Covers 21 <= hour < 24 and 0 <= hour < 7
        return f"Good night, {firstname}"

# Example usage
now = datetime.datetime.now()
hour = now.hour  # Automatically uses the current hour
firstname = input("What is your first name? ")
welcome = show_message(hour, firstname)
print(welcome)
