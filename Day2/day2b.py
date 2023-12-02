import re

file = open("input.txt")

content = file.readlines()

#for l in content: 
#    print(l)

#possibleGames = []

result = 0

minNumRed = [0] * (len(content)) 
minNumBlue = [0] * (len(content))
minNumGreen = [0] * (len(content))

for i in range(len(content)): 
      
    cnt = 0
    
    numSet = content[i].split(";")

    setRed = [0] * len(numSet)
    setBlue = [0] * len(numSet)
    setGreen = [0] * len(numSet) 

    for s in numSet: 
        #print(s)
        
        match = re.search(r'\d+ blue',s)
        if match:
   #         print(match[0])
            tmp = re.search(r'\d+',match[0])
            #print(cnt)
            setBlue[cnt] = int(tmp[0])
            
    
        match = re.search(r'\d+ red',s)
        if match:
  #          print(match[0])
            tmp = re.search(r'\d+',match[0])
            setRed[cnt] = int(tmp[0])
  
  

        match = re.search(r'\d+ green',s)
        if match:
 #           print(match[0])
            tmp = re.search(r'\d+',match[0])
            setGreen[cnt] = int(tmp[0])
        cnt += 1

    setRed.sort()
    setGreen.sort()
    setBlue.sort()

#    print(content[i])
#    print("r: ")
#    print(setRed)
#    print("g: ")
#    print(setGreen)
#    print("b: ")
#    print(setBlue)

    minNumRed[i] = setRed[len(numSet)-1]
    minNumGreen[i] = setGreen[len(numSet)-1]
    minNumBlue[i] = setBlue[len(numSet)-1]


for i in range(len(content)):
    result += minNumRed[i] * minNumGreen[i] * minNumBlue[i]

print(result)
