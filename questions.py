print("think of a character between wolverine, batman, doctor strange and superman")

question1 = input("does your character have superpowers?")
if question1 == "yes":
    print("i see")
    question2 = input("where they born with powers?")
    if question2 == "yes":
        print("if you say so")
        question3 = input("are they from another planet?")
        if question3 == "yes":
            print("youre thinking of superman")
        else:
            print("youre thinking of doctor strange")
            
    else:
        print("youre thinking of wolverine")
else:
    print("youre thinking of batman")


    
