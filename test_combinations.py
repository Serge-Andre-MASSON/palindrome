from combinations import Combination


def test_combination_product():
    content_0 = []
    
    combination_0 = Combination(content_0)
    assert combination_0.product == 0

    content_1 = [2, 5 ,3]
    
    combination_1 = Combination(content_1)
    assert combination_1.product == 30


def test_combination_is_palindrome():
    content_0 = [7]
    combination_0 = Combination(content_0)

    assert combination_0.is_palindrome()

    content_1 = [7, 2]
    combination_1 = Combination(content_1)

    assert not combination_1.is_palindrome()

    content_2 = [999, 989, 979]
    combination_2 = Combination(content_2)

    assert combination_2.is_palindrome()
    

def test_combination_comparisons():
    c_0 = Combination([4, 5, 6])
    c_1 = Combination([4, 10, 3])
    c_2 = Combination([4, 5, 7])

    assert c_0 == c_1
    assert c_2 > c_1

    

