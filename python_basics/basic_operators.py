"""The module contains basic operators exercises"""

# Arithmetic operators
number = 3 + 2 * 3 / 4
number_change_order = (3 + 2) * 3 / 4
remaider = 11 % 3
square = 2 ** 2
print(number)
print(number_change_order)
print(remaider)

# Operators with strings and lists
even = []
odd = []
_ = [even.append(x) if x % 2 == 0 else odd.append(x) for x in range(10)]
all_numbers = even + odd
print(all_numbers)
print(even * 3)

# Exercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print(f"x_list contains {len(x_list)} objects")
print(f"y_list contains {len(y_list)} objects")
print(f"big_list contains  {len(big_list)} objects")

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
