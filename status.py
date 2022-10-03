

def online_count(peopledictionary):
    count = 0
    for person in peopledictionary.items():
        if person[1] == 'online':
            print("found")
            count += 1
    return count

status = {"Alice": "online","Bob": "offline","Eve": "online"}
print(online_count(status))
