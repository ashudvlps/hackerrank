alphabetString = 'abcdefghijklmnopqrstuvwxyz'
alphaArray = []
for i in range(5,0,-1):
    for j in range(5,-1,-1):
        if i >j:
            alphaArray.append(alphabetString[j:i])
print(alphaArray)
