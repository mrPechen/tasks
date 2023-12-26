"""
Задача: 
Имеется список содержащий пары значений id, version, минимум 30 элементов.
Сгрупировать по уникальности пары id, version в list_version.
Вернуть набор сгруппированных значений в формате: [[id, version, count], …], 
Где count – количество одинаковых пар [id, version]
"""

test_arr = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]


def count(arr: list):
    a = dict()
    for i in arr:
        if i[0] in a.keys():
            if a[i[0]][0:-1] == i:
                a[i[0]][-1] += 1
            else:
                a[f'{i[0]}_{test_arr1.index(i)}'] = i
                a[f'{i[0]}_{test_arr1.index(i)}'].append(1)

        else:
            a[i[0]] = i
            a[i[0]].append(1)
    print(a.values())


count(test_arr)
