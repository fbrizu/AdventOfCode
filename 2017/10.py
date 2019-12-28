def p1():
    input = [int(i) for i in open('10').read().split(',')]
    l = [i for i in range(256)]
    curr = 0
    skip = 0
    for n in input:
        i1 = curr
        i2 = curr+n-1
        while i1 < i2:
            temp = l[i1 % len(l)]
            l[i1 % len(l)] = l[i2 % len(l)]
            l[i2 % len(l)] = temp
            i1 += 1
            i2 -= 1
        curr += n + skip
        skip += 1
    print(l[0] * l[1])

def p2():
    l = [i for i in range(256)]
    input = open('10').read()
    lengths = [ord(i) for i in input]
    lengths.append(17)
    lengths.append(31)
    lengths.append(73)
    lengths.append(47)
    lengths.append(23)
    curr = 0
    skip = 0
    for _ in range(64):
        for n in lengths:
            i1 = curr
            i2 = curr+n-1
            while i1 < i2:
                temp = l[i1 % len(l)]
                l[i1 % len(l)] = l[i2 % len(l)]
                l[i2 % len(l)] = temp
                i1 += 1
                i2 -= 1
            curr += n + skip
            skip += 1
    h = []
    for j in range(16):
        x = 0
        for i in range(16):
            if i == 0:
                x = l[j*16+i]
            else:
                x ^= l[j*16+i]
        h.append(x)
    a = ''
    for n in h:
        s = hex(n)[2:]
        if len(s) == 1:
            s = '0' + s
        a += s
    print(a)

p1()
p2()
