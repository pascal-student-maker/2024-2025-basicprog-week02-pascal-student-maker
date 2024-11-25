# Calculate the reaction distance
def reaction_distance(speed, reaction_time):
    """
    Calculates the reaction distance.
    :param speed: Speed in meters per second (m/s).
    :param reaction_time: Reaction time in seconds.
    :return: Reaction distance in meters.
    """
    return speed * reaction_time

# Calculate the braking distance
def braking_distance(speed, braking_deceleration):
    """
    Calculates the braking distance.
    :param speed: Speed in meters per second (m/s).
    :param braking_deceleration: Deceleration in meters per second squared (m/s^2).
    :return: Braking distance in meters.
    """
    return (speed ** 2) / (2 * braking_deceleration)

# Calculate the total stopping distance
def stopping_distance(speed, reaction_time, braking_deceleration):
    """
    Calculates the total stopping distance (reaction distance + braking distance).
    :param speed: Speed in meters per second (m/s).
    :param reaction_time: Reaction time in seconds.
    :param braking_deceleration: Deceleration in meters per second squared (m/s^2).
    :return: Total stopping distance in meters.
    """
    reaction_dist = reaction_distance(speed, reaction_time)
    braking_dist = braking_distance(speed, braking_deceleration)
    return reaction_dist + braking_dist

# Example usage
speed = float(input("Enter the speed in m/s: "))
reaction_time = float(input("Enter the reaction time in seconds: "))
braking_deceleration = float(input("Enter the braking deceleration in m/s^2: "))

total_stopping_distance = stopping_distance(speed, reaction_time, braking_deceleration)
print(f"The total stopping distance is {total_stopping_distance:.2f} meters.")
