def stopping_distance(speed, reaction_time, braking_deceleration):
    reaction_distance = speed * reaction_time
    braking_distance = speed**2 / (2 * braking_deceleration)
    return reaction_distance + braking_distance

# Get input from the user
speed = float(input("Enter the speed (in m/s): "))
reaction_time = float(input("Enter the reaction time (in seconds): "))
braking_deceleration = float(input("Enter the braking deceleration (in m/s^2): "))

# Calculate the stopping distance
total_stopping_distance = stopping_distance(speed, reaction_time, braking_deceleration)

print("The total stopping distance is:", total_stopping_distance, "meters")