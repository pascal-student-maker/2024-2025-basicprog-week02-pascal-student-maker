def create_welcome(name,classgroup="1CTAI1"):
    
    if classgroup not in ("1CTAI1","1MCT1"):
        classgroup = "1CTAI1"
    return f" Welcome {name} in {classgroup}"    

name = input("What is your name")
classgroup = input("What is your classgroup?")

create_welcome_in_class(name,classgroup)
 
