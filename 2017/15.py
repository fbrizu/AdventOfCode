def p1():
    f1 = 16807
    f2 = 48271
    g1 = 703
    g2 = 516
    count = 0
    for _ in range(40000000):
        g1 = g1 * f1 % 2147483647
        g2 = g2 * f2 % 2147483647
        if g1%65536 == g2%65536:
            count += 1
    print(count)

def p2():
    f1 = 16807
    f2 = 48271
    g1 = 703
    g2 = 516

    count = 0
    for _ in range(5000000):
        t1 = True
        t2 = True
        while t1 or g1%4 != 0:
            g1 = g1 * f1 % 2147483647
            t1 = False
        while t2 or g2%8 != 0:
            g2 = g2 * f2 % 2147483647
            t2 = False
        if g1%65536 == g2%65536:
            count += 1
    print(count)

p1()
p2()