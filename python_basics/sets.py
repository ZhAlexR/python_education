"""The exercises with sets here."""
string1 = "London is the capital of Great Britain"
string2 = "Berlin ist die Hauptstadt und die größte stadt in die Deutschland"

print(set(string1) - set(string2))
print(set(string1).difference(set(string2)))
print('______________________________________')

print(set(string1) | set(string2))
print(set(string1).union(set(string2)))
print('______________________________________')

print(set(string1) & set(string2))

print('______________________________________')
print(set(string1) ^ set(string2))
print(set(string1).symmetric_difference(set(string2)))

# exercise
# a = ["Jake", "John", "Eric"]
# b = ["John", "Jill"]
#
# print(set(a).difference(set(b)))
