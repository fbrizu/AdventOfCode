input = open('4').readlines()

def p1():
    count = 0
    for line in input:
        s = line.replace('[','-')
        s = s.replace(']','-')
        s = s.replace('\n','-')
        s = s.split('-')
        while '' in s:
            s.remove('')

        l = {}
        for i in range(len(s)-2):
            for c in s[i]:
                if c in l:
                    l[c] += 1
                else:
                    l[c] = 1
        l = {k:v for k,v in sorted(l.items(), key=lambda x: x[0])}
        l = {k:v for k,v in sorted(l.items(), key=lambda x: x[1], reverse=True)}
        
        checksum = ''
        ind = 0
        for kv in l:
            checksum += kv
            ind += 1
            if (ind == 5):
                break
        if checksum == s[-1]:
            count += int(s[-2])
    print(count)

def p2():
    for line in input:
        s = line.replace('[','-')
        s = s.replace(']','-')
        s = s.replace('\n','-')
        s = s.split('-')
        while '' in s:
            s.remove('')

        l = {}
        for i in range(len(s)-2):
            for c in s[i]:
                if c in l:
                    l[c] += 1
                else:
                    l[c] = 1
        l = {k:v for k,v in sorted(l.items(), key=lambda x: x[0])}
        l = {k:v for k,v in sorted(l.items(), key=lambda x: x[1], reverse=True)}
        
        checksum = ''
        ind = 0
        for kv in l:
            checksum += kv
            ind += 1
            if (ind == 5):
                break
        if checksum == s[-1]:
            msg = ''
            for i in range(len(s)-2):
                for c in s[i]:
                    msg += chr(ord('a') + ((ord(c) - ord('a') + int(s[-2])) % 26))
                msg += ' '
            #print(msg + ' ' + str(s[-2]))
            if 'northpole object storage' in msg:
                print(s[-2])

p1()
p2()