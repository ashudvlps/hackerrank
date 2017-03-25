from itertools import combinations
a = input().split()
L = sorted(a[0])
k = int(a[1])
P = []
for i in range(1,k+1):
    print("".join(P))
    for j in list(combinations(L,i)):
        P.append(j)
for m in j:
    print(m)
