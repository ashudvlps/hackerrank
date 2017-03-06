sourceInput = input()
checkInput = input()
lsi = len(sourceInput)
lci = len(checkInput)
a = 0
for i in range(0,len(sourceInput)-1):
    if checkInput == sourceInput[i:i+lci]:
        a+=1
print(a)
