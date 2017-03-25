a = input().split()
X=[]
for i in range(0,int(a[1])):
    X.append(list(map(float,input().split())))
for j in list(zip(*X)):
    print(sum(j)/len(j))
