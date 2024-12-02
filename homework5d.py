#homework 5d
def stopping_distance(speed,reaction_time,braking_deceleration) -> int:
 total = (speed * reaction_time) + (speed **2) / (2 * braking_deceleration)
 return total
 

result = stopping_distance(15,3,7)
print(f" the stopping distance is: {result}")
 
    

