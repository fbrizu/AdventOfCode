input = open('1').read()

def p1():
    ans = 0
    for c in input:
        if c == '(':
            ans += 1
        elif c == ')':
            ans -= 1
    print(ans)

def p2():
    ans = 0
    for i,c in enumerate(input):
        if c == '(':
            ans += 1
        elif c == ')':
            ans -= 1
            if ans == -1:
                print(i+1)
                break

p1()
p2()