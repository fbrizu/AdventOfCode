import hashlib

#id = 'abc'
id = 'cxdnnyjw'

def p1(input):
    password = ''
    it = 0
    while len(password) < 8:
        s = input + str(it)
        h = hashlib.md5(s.encode()).hexdigest()
        pw = True
        for i in range(5):
            if h[i] != '0':
                pw = False
                break
        if pw:
            password += h[5]
        it += 1
    print (password)

def p2(input):
    password = ['.','.','.','.','.','.','.','.']
    it = 0
    while '.' in password:
        s = input + str(it)
        h = hashlib.md5(s.encode()).hexdigest()
        pw = True
        for i in range(5):
            if h[i] != '0':
                pw = False
                break
        if pw:
            ind = int(h[5],16)
            if ind < len(password) and password[ind] == '.':
                password[ind] = str(h[6])
                #print(str(it) + ' ' + h[5] + ' ' + h[6])
        it += 1
    o = ''
    for i in range(len(password)):
        o += password[i]
    print (o)

#p1(id)
p2(id)