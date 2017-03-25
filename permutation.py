from itertools import permutations
a = input().split()
L = sorted(a[0])
k = int(a[1])
for i in list(permutations(L,k)):
    print("".join(i))
