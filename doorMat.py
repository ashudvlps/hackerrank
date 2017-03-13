N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print('{spr:-^{width}s}'.format(width=M, spr='.|.'*i))
print ('{spr:-^{width}s}'.format(width=M, spr='WELCOME'))
for i in range(N-2,-1,-2):
    print('{spr:-^{width}s}'.format(width=M, spr='.|.'*i))
