numberOfItems =input()
listOfHeight = input().split(" ")
heights = []
for i in listOfHeight:
    heights.append(int(i))
print(sum(set(heights))/len(set(heights)))
