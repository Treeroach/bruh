positive_feelings = ["happy","joy","gratitude","hope","love","awe","love","good","great"]

chat = ["hi!","hello!","how are you?","its been a while","good to see you"]

import random
num = random.randint(1,4)

print (chat[num])
question1 = input("my name is chatbot, what is your name?")

question2 = input("hello" + question1 + ", how are you feeling today?")

if question2 in positive_feelings:
    print("that is very good to hear!")
    sub1 = input("what is going on to make your day so good?")
    print(" lets hope it stays that way!")

elif question2 == "bad":
    print("aw that sucks to hear")
    sub2 = input ("what is happening to ruin your day?")
    print(" i hope your day can get better")

question3 = input("what is your favourite food?")


num2 = random.randint(1,5)

if num2 == "1":
    print(" no way me too!")
elif num2 == "2":
    print(" good choice ")
elif num2 == "3":
    print(" yuck! ")
elif num2 == "4":
    print(" not too fond myself but good choice! ")
elif num2 == "5":
    print("a what now? dont think ive ever heard of it")
