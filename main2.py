
def cycle_recover(cycle):  # функция для приведения списка связанности к виду, который требует степик
    result_str = str(cycle[0][0])+'->'+str(cycle[0][1])+'->'
    for i in range(1, len(cycle) - 1):
        result_str += str(cycle[i][1])
        result_str += '->'
    result_str += str(cycle[len(cycle) - 1][1])
    return result_str


def euler_cycle(connectivity_components, size):  # поиск эйлерова цикла в графе
    start = (0, connectivity_components[0][0])
    cycle = []  # стек в который записываются компоненты связанности цикла, который мы ищем
    bad_ways = set()  #
    counter = 0
    while True:
        counter += 1
        print(counter)
        while True:

            flag = False
            for s in connectivity_components[start[1]]:
                old_start = start
                start = (old_start[1], s)
                if start not in cycle and start not in bad_ways:
                    bad_ways.clear()
                    cycle.append(start)
                    flag = True
                    break
                else:
                    start = old_start
            if cycle[0][0] == start[1] or not flag:
                b = True
                for v in connectivity_components[start[1]]:
                    if (start[1], v) not in cycle:
                        start = (start[1], v)
                        cycle.append(start)
                        b = True
                        break
                    else:
                        b = False
                if not b:
                    break

        if len(cycle) == size:  # если найденый нами цикл обходит все ребра, то он эйлеров и работа функции завершена
            break

        for c in reversed(cycle):  # проходим по стеку с конца и ищем элемент, из которого мы можем пойти по другому
            # пути.
            for v in connectivity_components[c[0]]:
                flag = False
                edge = (c[0], v)
                if edge not in cycle and edge not in bad_ways:
                    cycle.pop()
                    cycle.append(edge)
                    start = edge
                    flag = True
                    break
            if flag == False:  # если мы не нашли куда можно перейти из текущего ребра в cycle, то мы удаляем это
                # ребро из cycle и записываем его в bad_ways, чтобы потом снова по нему не пойти
                bad_ways.add(edge)
                cycle.pop()
            else:
                break
    # эти два цикла чередуют друг друга. Сначала ищем какой-то цикл, и если он не эйлеров, то удаляем элементы из
    #     стека пока не дойдем до элемента, из которого можем продолжить цикл по другому пути
    #  в конечном итоге этот алгоритм должен привести нас к эйлерову пути
    return cycle


# Input ------------------------------------
def inp():
    connectivity_components = dict()
    tmp = []
    size = 0
    while True:
        line = input()
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
    result = cycle_recover(cycle)
    print(result)
