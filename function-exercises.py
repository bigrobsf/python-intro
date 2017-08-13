from __future__ import print_function


def difference(num1, num2):
    """This function returns the difference between two numbers"""
    return num1 - num2


def product(num1, num2):
    """This function returns the product of two numbers"""
    return num1 * num2


def print_day(num):
    """This function returns the day of the week corresponding to the number
    passed in"""
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    return days.get(num)


def last_element(my_list):
    """This function accepts a list as a parameter and returns the last item in
    the list"""
    if len(my_list) == 0:
        return None
    last = len(my_list) - 1
    return my_list[last]


def number_compare(num1, num2):
    """This function compares two numbers and returns a statement about which
    is greater"""
    if num1 > num2:
        return "First is greater."
    elif num2 > num1:
        return "Second is greater."
    return "Numbers are equal."


def single_letter_count(string, letter):
    """This function returns the number of times a letter appears in a
    string"""
    count = 0
    for char in string:
        if char.lower() == letter.lower():
            count += 1
    return count


def multiple_letter_count(string):
    """This function returns a dictionary containing the number of times
    each letter appears in a string"""
    return {char: string.count(char) for char in string}


def list_manipulation(a_list, command, location, *args):
    """This function performs list manipulation as determined by the supplied
    parameters"""
    if command == "remove":
        if location == "end":
            return a_list.pop()
        if location == "beginning":
            return a_list.pop(0)
    if command == "add":
        if location == "end":
            a_list.append(args[0])
            return a_list
        if location == "beginning":
            a_list.insert(0, args[0])
            return a_list


def is_palindrome(a_string):
    """This function detects if a word is a palindrome or not"""
    import math
    string = a_string.lower()
    a_list = string.split(' ')
    string = ''.join(a_list)
    length = len(string)
    test_length = math.floor(length / 2)
    for idx, char in enumerate(string):
        if idx < test_length:
            print(string[idx], string[length - 1 - idx])
            if string[idx] != string[length - 1 - idx]:
                return False
    return True


def frequency(a_list, value):
    """This function is the same as .count"""
    return a_list.count(value)


def flip_case(string, char):
    """This function changes the case of the character specified"""
    a_list = [letter.swapcase() if letter.lower() == char.lower() else letter
              for letter in string]
    return ''.join(a_list)


def multiply_even_numbers(a_list):
    """This function returns the product of all even numbers in a list"""
    product = 1
    for num in a_list:
        if num % 2 == 0:
            product *= num
    return product


def mode(a_list):
    """This function returns the most frequently occuring number in a list"""
    counter = {num: a_list.count(num) for num in a_list}
    highest = 0
    result = None

    for key, value in counter.items():
        if value > highest:
            highest = value
            result = key
    return result


def capitalize(string):
    """This function returns a single word in title case"""
    return string[0].upper() + string[1:].lower()


def compact(a_list):
    """This function returns a list of all the truthy values in a provided
     list"""
    return [value for value in a_list if value]


def partition(a_list, cb):
    """This function applies a callback to each element in a list and appends
    it to one of two lists depending on the result"""
    truthy_list = []
    falsey_list = []
    for val in a_list:
        if cb(val):
            truthy_list.append(val)
        else:
            falsey_list.append(val)
    return [truthy_list, falsey_list]


def intersection(lists):
    """This function returns a list of elements common to two lists"""
    return [value for value in lists[0] if value in lists[1]]




# end