import hashlib

input = 'qzyelonm'
#input = 'abc'

def p1():
    k = []
    ind = 0
    d = {}
    while len(k) < 100:
        s = input + str(ind)
        h = hashlib.md5(s.encode()).hexdigest()
        found = False
        repeat = 0
        old = ''
        for c in h:
            if c != old:
                old = c
                repeat = 1
            else:
                repeat += 1
                if repeat == 3:
                    if not found:
                        if not c in d:
                            d[c] = []
                        d[c].append(ind)
                    found = True
                if repeat == 5:
                    if c in d and len(d[c]) > 0:
                        for n in d[c]:
                            if n < ind and n >= ind-1000:
                                if not n in k:
                                    k.append(n)
        ind += 1
    k.sort()
    print(k[63])

def p2():
    k = []
    ind = 0
    d = {}
    while len(k) < 100:
        h = input + str(ind)
        for _ in range(2017):
            h = hashlib.md5(h.encode()).hexdigest()
        found = False
        repeat = 0
        old = ''
        for c in h:
            if c != old:
                old = c
                repeat = 1
            else:
                repeat += 1
                if repeat == 3:
                    if not found:
                        if not c in d:
                            d[c] = []
                        d[c].append(ind)
                    found = True
                if repeat == 5:
                    if c in d and len(d[c]) > 0:
                        for n in d[c]:
                            if n < ind and n >= ind-1000:
                                if not n in k:
                                    k.append(n)
        ind += 1
    k.sort()
    print(k[63])

p1()
p2()