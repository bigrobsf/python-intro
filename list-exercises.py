from __future__ import print_function

# 1
[print(num) for num in [1, 2, 3, 4]]

# 2
[print(num * 20) for num in [1, 2, 3, 4]]

# 3
initials = [val[0] for val in ['Elie', 'Tim', 'Matt']]

# 4
evens = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]

# 5
intersection = [num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6]]

# 6
result = [name[::-1].lower() for name in ['Elie', 'Tim', 'Matt']]

# 7
result = ''.join([letter for letter in 'first' if letter in 'third'])

# 8
result = [num for num in range(1, 100) if num % 12 == 0]

# 9
result = [letter for letter in 'amazing' if letter not in ['a', 'e', 'i', 'o', 'u']]

# 10
result = [[num for num in range(0, 3)]] * 3

# 11
result = [[num for num in range(0, 10)]] * 10
