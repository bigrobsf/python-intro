from __future__ import print_function

# 1
{key: value for (key, value) in [("name", "Elie"), ("job", "Instructor")]}

# 2
ab = ["CA", "NJ", "RI"]
states = ["California", "New Jersey", "Rhode Island"]
d = {ab[i]: states[i] for i in range(0, len(ab))}
print(d)

# or
dict(zip(ab, states))

# 3
{key: 0 for key in ['a', 'e', 'i', 'o', 'u']}

# 4
{num: chr(num + 64) for num in range(1, 27)}
