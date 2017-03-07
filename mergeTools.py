def merge_the_tools(string, k):
    nuSub = int(len(string)/k)
    for i in range(0,nuSub):
        text = string[(i)*k:(i+1)*k]
        textList = []
        for j in text:
            if j in textList:
                continue
            else:
                textList.append(j)
        print("".join(textList))
