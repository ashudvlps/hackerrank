values = 'Ashutosh Singh'
printList=[]
for val in values:
    if val.lower()==val:
        printList.append(val.upper())
    elif val.upper() == val:
        printList.append(val.lower())
    else:
        printList.append(val)
print "".join(printList)
