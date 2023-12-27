def func(a, b):
    #  Ключ: совп. индес; значение: совпадающая буква
    match = {i: a[i] for i in range(len(a)) if a[i] == b[i]}  # {1: 'а'}
    d = dict(zip(range(len(b)), b))
    d = {i: d[i] for i in d if i not in match.keys()}  # {0: 'т', 2: 'т', 3: 'а', 4: 'м', 5: 'и'}
    d2 = {}
    # new_b = [element for i, element in enumerate(b) if i not in match.keys()] # т т а м и
    new_a = [element for i, element in enumerate(a) if i not in match.keys()]  # г з е т а
    #  совпадающие по значению, не по индексу
    for ind, letter in d.items():
        if letter in new_a:
            d2[ind] = letter
    print(d2)  # подсветка синим
    print('полное совпадение:', match)  # подсветка красным
    return match, d2

#  г а з е т а
#  т а т а м и
