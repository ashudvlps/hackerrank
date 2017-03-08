def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
inputString ="BANANA"
vowelList = ['A','E','I','O','U']
kevin = []
stuart = []
for i in range(0,len(inputString)):
    # print(inputString[i])
    if inputString[i] in vowelList:
        for j in range(1,len(inputString)+1):
            kevin.append(inputString[i:i+j])
    else:
        for j in range(1,len(inputString)+1):
            stuart.append(inputString[i:i+j])

kevinList = set(kevin)
stuartList = set(stuart)
kevinScore = 0
stuartScore = 0
for k in kevinList:
    kevinScore+=occurrences(inputString,k)
for l in stuartList:
    stuartScore+=occurrences(inputString,l)
if kevinScore>stuartScore:
    print("Kevin {}".format(kevinScore))
elif kevinScore<stuartScore:
    print("Stuart {}".format(stuartScore))
else:
    print("Draw")
