def Descending_Order(num):
    a_list = list(str(num))
    a_list.sort(reverse=True)
    sorted_num = ''.join(a_list)
    return int(sorted_num)


def createDict(keys, values):
    return {keys[idx]: (values[idx] if idx < len(values) else None)
            for idx in range(0, len(keys))}


def bonus_time(salary, bonus):
    return '$' + str(salary * 10) if bonus else '$' + str(salary)


def always(n=0):
    def inner():
        return n
    return inner


def powers_of_two(n):
    return [pow(2, num) for num in range(0, n + 1)]


def remove_every_other(my_list):
    idx = 1
    while idx < len(my_list):
        my_list.pop(idx)
        idx += 1
    return my_list


def count_by(x, n):
    return [num * x for num in range(1, n + 1)]


def positive_sum(arr):
    sum = 0
    for num in arr:
        if num > 0:
            sum += num
    return sum


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {}!".format(name)


def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'


def position(alphabet):
    letters = [chr(num) for num in range(97, 123)]
    return 'Position of alphabet: {}'.format(letters.index(alphabet) + 1)


def toJadenCase(string):
    return ' '.join([word.capitalize() for word in string.split(' ')])


def find_needle(haystack):
    return 'found the needle at position ' + str(haystack.index('needle'))


def in_array(a1, a2):
    result = []
    for sub in a1:
        for word in a2:
            if sub in word and sub not in result:
                result.append(sub)
    return result


def bumps(road):
    return 'Car Dead' if road.count('n') > 15 else "Woohoo!"


def get_middle(s):
    length = len(s)
    mid_point = int(length / 2)
    if length % 2 == 0:
        return s[mid_point - 1: mid_point + 1]
    else:
        return s[mid_point: mid_point + 1]


def high_and_low(numbers):
    a_list = [int(num) for num in numbers.split(' ')]
    return '{} {}'.format(str(max(a_list)), str(min(a_list)))


def is_isogram(string):
    s = set(string.lower())
    return True if len(string) == len(s) else False


def square_digits(num):
    nums = list(str(num))
    sq_list = [str(int(n)**2) for n in nums]
    return int(''.join(sq_list))
