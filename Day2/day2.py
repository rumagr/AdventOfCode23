import re

MAX_NUM_RED = 12
MAX_NUM_GREEN = 13
MAX_NUM_BLUE = 14

file = open("input.txt")

content = file.readlines()

#for l in content: 
#    print(l)

#possibleGames = []

result = 0

gameNumbers = [0] * (len(content)-1) 

for i in range(len(content)): 

    numSet = content[i].split(";")

    for s in numSet: 
    #print(s)
        match = re.search(r'\d+ blue',s)
        if match:
   #         print(match[0])
            tmp = re.search(r'\d+',match[0])
            num = int(tmp[0])
            if(num > MAX_NUM_BLUE):
                gameNumbers[i] = 1
                break 
    
        match = re.search(r'\d+ red',s)
        if match:
  #          print(match[0])
            tmp = re.search(r'\d+',match[0])
            num = int(tmp[0])
            if(num > MAX_NUM_RED):
                gameNumbers[i] = 1
                break

        match = re.search(r'\d+ green',s)
        if match:
 #           print(match[0])
            tmp = re.search(r'\d+',match[0])
            num = int(tmp[0])
            if(num > MAX_NUM_GREEN):
                gameNumbers[i] = 1
                break

for i in range(len(gameNumbers)):
    if(not gameNumbers[i]):
        #possibleGames.append(i+1)
        result += (i+1)

print(result)

#print(gameNumbers)
#print(possibleGames)
