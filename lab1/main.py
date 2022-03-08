from math import sqrt, pow
from queue import PriorityQueue


# Problem 1:
def get_last_alphabetic_word(phrase):
    words = phrase.split()
    if len(words) <= 1:
        return phrase
    # default sorting of string list is alphabetical
    return sorted(words)[-1]


# Problem 1 test
def test_get_last_alphabetic_word():
    assert get_last_alphabetic_word('Ana are mere rosii si galbene') == 'si'
    assert get_last_alphabetic_word('') == ''
    assert get_last_alphabetic_word('Some other text with 23 numbers') == 'with'


# Problem 2
def get_distance(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


# Problem 2 test
def test_get_distance():
    assert get_distance(1, 5, 4, 1) == 5
    assert get_distance(4.5, 5.1, -3, 3.2) == 7.73692445355388
    assert get_distance(0, 0, 0, 0) == 0


# Problem 3
# function is case sensitive!
def get_min_word_count(phrase):
    word_count = {}
    for word in phrase.split():
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    result_words = []
    for word in word_count:
        if word_count[word] == 1:
            result_words.append(word)

    return result_words


# Problem 4 test
def test_get_min_word_count():
    assert get_min_word_count('ana are ana are mere rosii ana') == ['mere', 'rosii']
    assert get_min_word_count('') == []
    assert get_min_word_count('Sase sasi in sase saci') == ['Sase', 'sasi', 'in', 'sase', 'saci']


# Problem 5
def get_duplicate_number(array):
    dict = {}
    for number in array:
        if number in dict:
            return number
        else:
            dict[number] = 1
    return 'No duplicate number!'


# Problem 5 test
def test_get_duplicate_number():
    assert get_duplicate_number([1, 2, 3, 4, 3]) == 3
    assert get_duplicate_number([1, 2, 2]) == 2
    assert get_duplicate_number([1, 2, 3, 4]) == 'No duplicate number!'


# Problem 6
def get_major_number(array):
    half_array_len = len(array) / 2
    dict = {}

    for number in array:
        if number in dict:
            if dict[number] + 1 >= half_array_len:
                return number
            else:
                dict[number] = dict[number] + 1
        else:
            if 1 > half_array_len:
                return number
            dict[number] = 1

    return 'No major number!'


# Problem 6 test
def test_get_major_number():
    assert get_major_number([1, 2, 1, 2, 1, 3, 1]) == 1
    assert get_major_number([4]) == 4
    assert get_major_number([1, 2, 3, 4, 5]) == 'No major number!'


# Problem 7
def get_k_biggest_number(array, k):
    if k > len(array) or k < 1:
        return 'Invalid k value!'

    queue = PriorityQueue()
    for number in array:
        queue.put(-number)  # negate the number to reverse the actual order of numbers

    while k > 0:
        result = -queue.get()
        k -= 1
    return result


# Problem 7 test
def test_get_k_biggest():
    assert get_k_biggest_number([3, 1, 6, 8, 23], 2) == 8
    assert get_k_biggest_number([3, 1, 6, 8, 23], 7) == 'Invalid k value!'
    assert get_k_biggest_number([3, 1, 6, 2], 1) == 6
    assert get_k_biggest_number([3, 1, 6, 2], 4) == 1


# Problem 8
def generate_binary_nums(nr):
    bin_nums = []
    k = 1

    while len(bin_nums) < nr:
        if len(bin_nums) == 0:
            bin_nums.append(k)
            k *= 10
            continue  # needed for case when nr = 1
        bin_nums.append(k)
        for number in bin_nums[:len(bin_nums) - 1]:
            if len(bin_nums) == nr:
                return bin_nums
            bin_nums.append(number + k)
        k *= 10
    return bin_nums


# Problem 8 test
def test_generate_binary_nums():
    assert generate_binary_nums(5) == [1, 10, 11, 100, 101]
    assert generate_binary_nums(10) == [1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010]
    assert generate_binary_nums(0) == []
    assert generate_binary_nums(1) == [1]


# Run all the tests
def run_tests():
    test_get_last_alphabetic_word()
    test_get_distance()
    test_get_min_word_count()
    test_get_duplicate_number()
    test_get_major_number()
    test_get_k_biggest()
    test_generate_binary_nums()


run_tests()
