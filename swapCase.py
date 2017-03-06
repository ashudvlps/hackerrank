values = input()
upperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
printList = []
# def swap_case(s):
for val in values:
        if val in upperList:
            printList.append(val.lower())
        elif val in lowerList:
            printList.append(val.upper())
        else:
            printList.append(val)
print("".join(printList))
