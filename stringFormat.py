def print_formatted(number):
    w = int(len(str("{0:b}".format(number))))+1
    for i in range(1,number+1):
        d = str("{0:d}".format(i))
        o = str("{0:o}".format(i))
        h = str("{0:X}".format(i))
        b = str("{0:b}".format(i))
        print("{:>}{:>{w}}{:>{w}}{:>{w}}".format(d,o,h,b,w=w))
print_formatted(10)
print(5)
