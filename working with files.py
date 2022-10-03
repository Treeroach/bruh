def write():
    with open("data.txt","w") as file:
        file.close()

def read():
    with open("data.txt","r") as file:
        file.close()

def append():
    with open("data.txt","a") as file:
        file.close()

write()
