"""The module contains list exercises"""
# append and index
mylist = []
mylist.append(1)
mylist.append("two")
mylist.append("orange")
print(mylist[0])
print(mylist[1])
print(mylist[-2])
# for x in mylist:
#     print(x)

# append vs extend
new_list = [7, 8, "sky", "snow"]
mylist.append(new_list)
print(mylist)
mylist.extend(new_list)
print(mylist)

# slicing
print(mylist[0:4])
print(mylist[-3:])
print(mylist[3][2])

# insert, remove, pop, clear
mylist.insert(0, "FIRST PLACE!")
mylist.remove("sky")
mylist[4].pop(2)
print(mylist)
mylist.extend([1, "two"] * 3)

# count, sort, reverse
print(mylist.count("two"))
string_list = [x for x in mylist if isinstance(x, str)]
string_list.sort()
print(string_list)
