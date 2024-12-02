def create_welcome_in_class(name:str,classgroup= "1CTAI1")->  str:
    print(f"Welcome {name} in {classgroup}.")
    
name = input("What is your name?")    
classgroup = input("What is your classgroup?")

create_welcome_in_class(name,classgroup)
 
