for i in range(1,int(input())+1):
    print(''.join(str(j) for j in range(1,i+1))+''.join(str(j) for j in range(i-1,0,-1)))
