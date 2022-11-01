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
