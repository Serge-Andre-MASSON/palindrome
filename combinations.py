from functools import reduce
from operator import mul


class Combination(list):
    def __init__(self, content: list):
        super(Combination, self).__init__(content)
        try:
            self.product = reduce(mul, self)
        except TypeError:
            self.product = 0

    def is_palindrome(self):
        s = str(self.product)
        return s == s[::-1]

    def __eq__(self, other: "Combination"):
        return self.product == other.product
        
    def __gt__(self, other: "Combination"):
        return self.product > other.product



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
