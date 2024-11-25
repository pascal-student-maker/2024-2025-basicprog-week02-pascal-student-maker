import math
score = float(input("Enter your test score (out of 20):"))
if score - int(score) < 0.5:
    rounded_score = math.floor(score)
else:
    rounded_score = math.ceil(score)
print("Your rounded score is:",rounded_score)

if rounded_score >= 10:
    print("Congratulations you passed !")
else:
    print("unfortunalety you didnt pass better luck next time!")
    
    #my code 
    
    

#exercise 05

x = int(input("enter your test score":))

if score >= 10:

 print((math.floor(x))"congratuations , you passed")

else:

 print((math.ceil(x))" Alas,better luck next time")
