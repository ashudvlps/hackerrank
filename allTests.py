# def validateFactor(num,f):
#     for i in range(1,num+1):
#         if num%f==0:
#             return True
#         else:
#             return False
# print(validateFactor(int(input()),int(input())))
inString = input()
inFactor = int(input())
nuSub = int(len(inString)/inFactor)

for i in range(0,nuSub):
    text = inString[(i)*inFactor:(i+1)*inFactor]
    textList = []
    for j in text:
        if j in textList:
            continue
        else:
            textList.append(j)
    print("".join(textList))
    # print(set(text))
    # pList.append("".join())
    # print(pList)
