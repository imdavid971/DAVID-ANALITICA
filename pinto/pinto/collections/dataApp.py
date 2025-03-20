from data import personas
#print(data.personas)
for dict in personas:
    for key in dict.keys():
        if key=="name":
            print(dict[key])