def include(a, b):
    for i in b:
        if i in a:
            a.remove(i)
    if len(a) == 0:
        return True
    else:
        return False


def cycle_recover(cycle):
    result_str = str(cycle[0][0])+'->'+str(cycle[0][1])+'->'
    for i in range(1, len(cycle) - 1):
        result_str += str(cycle[i][1])
        result_str += '->'
    result_str += str(cycle[len(cycle) - 1][1])
    return result_str


def euler_cycle(connectivity_components):
    start = connectivity_components[0]
    cycle = [start]
    bad_ways = set()
    counter = 0
    while True:
        # for i in range(len(connectivity_components)):
        for edge in connectivity_components:
            if start[1] == edge[0] and edge not in cycle and edge not in bad_ways:
                cycle.append(edge)
                start = edge
                bad_ways.clear()
                break
        if len(cycle) == len(connectivity_components):
            break

        for c in reversed(cycle):
            for ed in connectivity_components:
                flag = False
                if c[1] == ed[0] and ed not in cycle and ed not in bad_ways:
                    start = c
                    flag = True
                    break
            if flag == False:
                bad_ways.add(c)
                cycle.pop()
            else:
                break
        if counter == 500:
            print(101)
    return cycle


# Input ------------------------------------
def inp():
    connectivity_components = []
    while True:
        line = input()
        if line:
            line = line.split('->')
            str1 = line[1].split(',')
            for s in str1:
                connectivity_components.append((int(line[0]), int(s)))
        else:
            break
    return connectivity_components
# ---------------------------------------------


if __name__ == '__main__':
    connectivity_components = inp()
    # connectivity_components = [(0, 3), (1, 12), (1, 2), (10, 1), (11, 10), (12, 11), (13, 3), (14, 13), (15, 14), (2, 0), (2, 4), (3, 1), (3, 15), (4, 6), (4, 7), (5, 2), (6, 5), (7, 9), (8, 4), (9, 8)]
    cycle = euler_cycle(connectivity_components)
    result = cycle_recover(cycle)
    print(result)
