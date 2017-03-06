n = int(input())+1
w = int(len(str("{0:b}".format(n))))+1
for i in range(1,n):
    d = str("{0:d}".format(i))
    o = str("{0:o}".format(i))
    h = str("{0:X}".format(i))
    b = str("{0:b}".format(i))
    print("{0:>{w}}{1:>{w}}{2:>{w}}{3:>{w}}".format(d,o,h,b,w=w))
