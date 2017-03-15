alphabetString = 'abcdefghijklmnopqrstuvwxyz'
def parray(number):
    alphaArray = []
    for i in range(number,0,-1):
        print(alphabetString[i])
        alphaArray.append(alphabetString[i])
    for j in range(0,number-1):
        print(alphabetString[j])
        alphaArray.append(alphabetString[j])
    return '-'.join(alphaArray)
n = int(input())
w = 4*n-3
h = 2*n-1
seq = list(range(1,n))+list(range(n,0,-1))
# print(seq)
for i in seq:
    print('{spr:-^{w}s}'.format(w=w,spr=parray(i)))
