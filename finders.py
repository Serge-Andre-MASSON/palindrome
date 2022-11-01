from abc import ABC, abstractmethod
from combinations import Combination

from iterators import get_ordered_iterator, get_naive_iterator, get_pruned_iterator


class PalindromeFinder(ABC):
    def __init__(self, min_digit, max_digit, n_digits=3):
        self.min_digit = min_digit
        self.max_digit = max_digit
        self.n_digits = n_digits
        self.biggest_combination = Combination([min_digit]*n_digits)

    @abstractmethod
    def find(self):
        pass


class NaiveFinder(PalindromeFinder):
    def find(self):
        combinations_iterator = get_naive_iterator(
            self.min_digit,
            self.max_digit,
            self.n_digits)

        for combination in combinations_iterator:
            if combination.is_palindrome() and combination > self.biggest_combination:
                self.biggest_combination = combination

        return self.biggest_combination.product


class PrunedFinder(PalindromeFinder):
    def find(self):
        combinations_iterator = get_pruned_iterator(
            self.min_digit,
            self.max_digit)

        for combination in combinations_iterator:
            if combination.is_palindrome():
                self.biggest_combination = combination

        return self.biggest_combination.product


class OrderedFinder(PalindromeFinder):
    def find(self):
        combinations_iterator = get_ordered_iterator(
            self.min_digit,
            self.max_digit,
            self.n_digits)

        for combination in combinations_iterator:
            if combination.is_palindrome():
                return combination.product
