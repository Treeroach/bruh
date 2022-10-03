keys = ["ten","twenty", "thirty"]
values = [10,20,30]

dictionary = dict(zip(keys,values))

print(dictionary)



sampledict = {
    "class":{
        "student":{
            "name":"mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}


print(sampledict["class"]["student"]["marks"]["history"])


sampledict2 = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "new york"

}
keystoremove = ["name", "salary"]


del (sampledict[keystoremove])
print(sampledict)
