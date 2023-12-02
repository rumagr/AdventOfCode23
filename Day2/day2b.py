import re

file = open("test_data_b.txt")

content = file.readlines()

#for l in content: 
#    print(l)

#possibleGames = []

result = 0

minNumRed = [0] * (len(content)) 
minNumBlue = [0] * (len(content))
minNumGreen = [0] * (len(content))

for i in range(len(content)): 
    
    setRed = [0] * 3
    setBlue = [0] * 3 
    setGreen = [0] * 3   
    cnt = 0
    
    numSet = content[i].split(";")

    for s in numSet: 
    #print(s)
        
        match = re.search(r'\d+ blue',s)
        if match:
   #         print(match[0])
            tmp = re.search(r'\d+',match[0])
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

    minNumRed[i] = setRed[2]
    minNumGreen[i] = setGreen[2]
    minNumBlue[i] = setBlue[2]


for i in range(len(content)):
    result += minNumRed[i] * minNumGreen[i] * minNumBlue[i]

print(result)
