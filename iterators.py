from collections import deque
from itertools import combinations_with_replacement

from combinations import Combination


def get_naive_iterator(min_digit: int, max_digit: int, n_digits: int):
    atomic_iterator = range(max_digit, min_digit, -1)
    for combination in combinations_with_replacement(atomic_iterator, n_digits):
        yield Combination(combination)


def get_pruned_iterator(min_digit, max_digit):
    biggest_palindrome = 0
    for i in range(max_digit, min_digit, -1):
        for j in range(i, min_digit, -1):
            for k in range(j, min_digit, -1):
                combination = Combination([i, j, k])
                if combination.product < biggest_palindrome:
                    break
                if combination.is_palindrome():
                    biggest_palindrome = combination.product
                yield combination


def get_ordered_iterator(min_digit, max_digit, n_digits, almost=False):
    combination = Combination([max_digit]*n_digits)
    combinations = deque([combination])

    layer = [combination]
    layers = get_layers(layer, min_digit)

    while combinations:
        combination = combinations.popleft()
        yield combination

        if combination == layer[0]:
            try:
                layer = next(layers)
                if almost:
                    combinations.extend(layer)
                else:
                    combinations = merge(combinations, layer)
            except StopIteration:
                continue


def merge(list_1: deque[Combination], list_2: list[Combination]):
    if not list_1:
        return deque(list_2)
    for el in list_2:
        l = len(list_1)
        j = l-1
        while el > list_1[j]:
            j -= 1
        list_1.insert(j + 1, el)
    return list_1

def get_layers(layer: list[Combination], min_: int):
    while layer:
        next_layer = []
        last_products = [c.product for c in layer]
        for combination in layer:
            for next_combination in next_combinations(combination, min_):
                n = next_combination.product
                if n in last_products:
                    pass
                else:
                    last_products.append(n)
                    next_layer.append(next_combination)
        layer = next_layer
        if layer:
            yield layer


def next_combinations(c: Combination, min_: int):
    l = len(c)
    for i, el in enumerate(c):
        tmp = c.copy()
        if i < l - 1:
            if el > c[i + 1]:
                tmp[i] = max(el - 1, min_)
                yield Combination(tmp)
        else:
            tmp[i] = max(el - 1, min_)
            yield Combination(tmp)


