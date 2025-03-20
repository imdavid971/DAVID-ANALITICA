with open("files/data.txt","r") as data:
    line=data.readlines()
    #while line !="":
    print(type(line))
    print(line[0])
    print(type(line[0]))
    print(line[0].split(",")[0])
    # print(line[0].split()[0])
    # print(line[0].split()[1])
    # print(line[0].split()[2])
    # tam=len(line[0].split()[0])
    # thename=line[0].split()[0]
    # print(thename[1:tam])
    # print("name" in line[0])
    
    # for palabra in line[0]:
    #     print(palabra)
        
        #line=data.readline()

