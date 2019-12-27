input = open('10').readlines()
#input = open('10_2').readlines()

def p1():
    ins = []
    bots = {}
    output = {}
    for line in input:
        ins.append(line.strip())
        ind = 0
    while len(ins) > 0:
        s = ins[ind]
        if s.startswith('value'):
            s = s.split()
            v = int(s[1])
            b = int(s[5])
            if not b in bots:
                bots[b] = []
            bots[b].append(v)
            ins.remove(ins[ind])
            ind = 0
            continue
        else:
            s = s.split()
            b = int(s[1])
            if not b in bots:
                ind += 1
                continue
            elif len(bots[b]) < 2:
                ind += 1
                continue
            if min(bots[b]) == 17 and max(bots[b]) == 61:
                print(b) #p1
            v1 = int(s[6])
            v2 = int(s[11])
            if s[5] == 'bot':
                if not v1 in bots:
                    bots[v1] = []
                bots[v1].append(min(bots[b]))
            else:
                if not v1 in output:
                    output[v1] = []
                output[v1].append(min(bots[b]))
            if s[10] == 'bot':
                if not v2 in bots:
                    bots[v2] = []
                bots[v2].append(max(bots[b]))
            else:
                if not v2 in output:
                    output[v2] = []
                output[v2].append(max(bots[b]))
            bots[b] = []
            ins.remove(ins[ind])
            ind = 0
            continue
        ind += 1
    #print(bots)
    #print(output)
    print(output[0][0] * output[1][0] * output[2][0])

p1()