# Solution to the problem of list in hacker rank
# https://www.hackerrank.com/challenges/python-lists
N = int(input())
flist = []
templist = []
for i in range(0,N):
    inp = input()
    inpl = inp.split(' ')
    if inpl[0]=='insert':
        templist.insert(int(inpl[1]),int(inpl[2]))
    elif inpl[0]=='print':
        flist.append(tuple(templist))
    elif inpl[0]=='remove':
        templist.remove(int(inpl[1]))
    elif inpl[0]=='append':
        templist.append(int(inpl[1]))
    elif inpl[0]=='sort':
        templist.sort()
    elif inpl[0]=='pop':
        templist.pop()
    elif inpl[0]=='reverse':
        templist.reverse()
for rows in flist:
    print(list(rows))
