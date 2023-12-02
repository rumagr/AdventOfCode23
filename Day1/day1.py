import re 

file = open("input.txt")

content = file.readlines()

dSpelled = ["one","two","three","four","five","six","seven","eight","nine"]
digit = ["1","2","3","4","5","6","7","8","9"]

dMap = dict(zip(dSpelled,digit))

foo = 0; 

print(dMap)

for i in range(len(content)):
    for a in range(len(content[i])):
        for y in dSpelled:
            if y in content[i][0:a]:
                content[i] = content[i].replace(y,dMap[y]) 
                foo = 1                
                break
        if foo > 0: 
            foo = 0
            break

for i in range(len(content)):
    for a in range(len(content[i])):
        b = len(content[i])-a        
        for y in dSpelled:
            if y in content[i][b:len(content[i])]:
                content[i] = content[i].replace(y,dMap[y])                
                foo = 1                
                break
        if foo > 0: 
            foo = 0 
            break            



num = [] 

res = 0
 
p = r'\d'

for x in content: 
    print(x)
    if re.search(p, x) is not None: 
        for catch in re.finditer(p, x):      
            num.append(catch[0])
    #print(num)
    if len(num) > 1: 
        temp = int(num[0])*10 + int(num[len(num)-1]) 
        res += temp
        print(temp)        
    elif len(num) == 1: 
        temp = int(num[0])*10 + int(num[0])
        res += temp
        print(temp)        
    num.clear()

print(res)
