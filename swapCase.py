# You are given a string S. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
values = input()
printList=[]
for val in values:
    if val.islower():
        printList.append(val.upper())
    elif val.isupper():
        printList.append(val.lower())
    else:
        printList.append(val)
print ("".join(printList))
