#exercise 3a
import datetime 
c  = datetime.datetime.now().year
d = datetime.datetime.now().month
a = int(input(" What is your year of birth?"))
b = int(input(" What is your month of birth?"))
if (c- a > 18): print("You are over 18 so you are allowed to drink alcohol in Belgium.")
elif (c-a == 18 and  b<= d): print("You are 18 and you are allowed to drink alcohol in Belgium.")
else: print("You are under 18, so you cannot drink alcohol in Belgium!")
