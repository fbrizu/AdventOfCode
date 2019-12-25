input = open('7').readlines()

def p1():
    count = 0
    for line in input:
        s = line.strip()
        s = s.replace('[', ']')
        s = s.split(']')
        foundOut = False
        foundIn = False
        for ind,w in enumerate(s):
            if foundIn:
                break
            for i in range(len(w)):
                if i < 3:
                    continue
                if w[i]==w[i-3] and w[i-1]==w[i-2] and w[i]!=w[i-1]:
                    if ind % 2 == 0:
                        foundOut = True
                    else:
                        foundIn = True
        if foundOut and not foundIn:
            count += 1
    print(count)

def p2():
    count = 0
    for line in input:
        s = line.strip()
        s = s.replace('[', ']')
        s = s.split(']')
        aba = [] #(a,b)
        found = False
        for ind,w in enumerate(s):
            if ind % 2 == 1:
                continue
            for i in range(len(w)):
                if i < 2:
                    continue
                if w[i]==w[i-2] and w[i]!= w[i-1]:
                    aba.append((w[i],w[i-1]))
        for ind,w in enumerate(s):
            if ind % 2 == 0:
                continue
            for i in range(len(w)):
                if i < 2:
                    continue
                for (a,b) in aba:
                    if w[i]==b and w[i-1]==a and w[i-2]==b:
                        found = True
        if found:
            count += 1
            #print(s)
    print(count)

p1()
p2()