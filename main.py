import sys
from collections import deque


def euler_cycle(connectivity_components, size):  # поиск эйлерова цикла в графе
    stack = deque()
    stack.append(0)
    cycle = []
    while len(stack) != 0:
        v = stack.pop()
        stack.append(v)
        if v == 0:
            print(101)
        if len(connectivity_components[v]) == 0:
            cycle.append(v)
            stack.pop()
        else:
            stack.append(connectivity_components[v][0])
            connectivity_components[v].remove(connectivity_components[v][0])
    return cycle


# Input ------------------------------------
def inp():
    connectivity_components = dict()
    tmp = []
    size = 0
    for line in sys.stdin:
        if line:
            line = line.split('->')
            str1 = line[1].split(',')
            tmp.clear()
            for s in str1:
                tmp.append(int(s))
                size += 1
            connectivity_components[int(line[0])] = tmp.copy()
        else:
            break
    return connectivity_components, size
# ---------------------------------------------


if __name__ == '__main__':
    connectivity_components, size = inp()  # список связанности
    cycle = euler_cycle(connectivity_components, size)
    cycle.reverse()
    print("->".join(map(str, cycle)))
