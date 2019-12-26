import copy

screen = []
xlen = 50
ylen = 6

def print_screen():
    for r in screen:
        for c in r:
            if c:
                print('#', end='')
            else:
                print(' ', end='')
        print('\n', end='')
    print('')

def solve():
    input = open('8').readlines()
    global screen
    for j in range(ylen):
        screen.append([])
        for i in range(xlen):
            screen[j].append(False)
    for line in input:
        line = line.strip()
        w = line.split()
        if line.startswith('rect'):
            s = w[1].split('x')
            for j in range(int(s[1])):
                for i in range(int(s[0])):
                    screen[j][i] = True
        elif line.startswith('rotate column'):
            temp = copy.deepcopy(screen)
            c = int(w[2].split('=')[1])
            offset = int(w[4])
            #print(str(c) + ' ' + str(offset))
            for y in range(ylen):
                temp[y][c] = screen[(y+ylen-offset)%ylen][c]
            screen = copy.deepcopy(temp)
        elif line.startswith('rotate row'):
            temp = copy.deepcopy(screen)
            r = int(w[2].split('=')[1])
            offset = int(w[4])
            #print(str(r) + ' ' + str(offset))
            for x in range(xlen):
                temp[r][x] = screen[r][(x+xlen-offset)%xlen]
            screen = copy.deepcopy(temp)
        #print_screen()
    print_screen()
    count = 0
    for j in range(ylen):
        for i in range(xlen):
            if screen[j][i]:
                count += 1
    print(count)

solve()