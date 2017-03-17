from itertools import product
A = map(int,input().split())
B = map(int,input().split())
P = []
for i in list(product(A,B)):
    P.append(str(i))
print(" ".join(P))
