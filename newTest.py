str = "ashutoshsingh"
strList = []
for i in str:
    if i in strList:
        break
    else:
        strList.append(i)
print("".join(strList))
