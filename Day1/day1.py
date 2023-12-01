import re 

file = open("input.txt")

content = file.readlines()

num = [] 

res = 0
 
p = r'\d'

for x in content: 
    print(x)
    if re.search(p, x) is not None: 
        for catch in re.finditer(p, x):      
            num.append(catch[0])
    print(num)
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
