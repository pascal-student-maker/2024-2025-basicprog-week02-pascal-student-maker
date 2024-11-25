import datetime

# Function to show the appropriate message based on the hour
def def_show_message(hour, firstname):
    # Check the time range and print the appropriate message
    if 7 <= hour < 12:  # 7:00 to 11:59
        message = f"Good Morning, {firstname}!"
    elif 12 <= hour < 13:  # 12:00 to 12:59
        message = f"It's Noon, {firstname}!"
    elif 13 <= hour < 17:  # 13:00 to 16:59
        message = f"Good Afternoon, {firstname}!"
    elif 17 <= hour < 21:  # 17:00 to 20:59
        message = f"Good Evening, {firstname}!"
    else:  # 21:00 to 6:59
        message = f"Good Night, {firstname}!"
    
    return message

# Main script to ask for user input
try:
    # Get the current time
    current_time = datetime.datetime.now()
    hour = current_time.hour  # Extract the hour from the current time

    # Get the user's name
    firstname = input("What is your first name? ")

    # Call the function and print the message
    welcome_message = def_show_message(hour, firstname)
    print(welcome_message)

except Exception as e:
    print(f"An error occurred: {e}")
