#exercise 4b
a = int(input(" enter the age of your dog?"))
if (a <= 0 ): print(" error message age is not possible")
elif( a == 1): print(" your dog is 14 in human years!")
elif ( a ==2): print( "Your dog is 22 in human years!")
else: print(f" Your dog is   {22+(a-2)*5} in human years!")
