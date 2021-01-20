"""
Manipulating lists
"""


numlist = [1, 2, 3, 4, 5]

print(numlist)

numlist.reverse()
print(numlist)

numlist.sort()
print(numlist)

for num in numlist:
    print(str(num))

mystring = 'julian'
mystring_list = list(mystring)
print(mystring_list)

print(mystring_list[4])
print(mystring_list.pop())

print(mystring_list)
mystring_list.insert(5, 'n')

print(mystring_list)
mystring_list[0] = 'b'
print(mystring_list)

del mystring_list[0]
print(mystring_list)

mystring_list.insert(0, 'm')
print(mystring_list)

print(mystring_list.pop(0))
print(mystring_list)

mystring_list.append('s')
print(mystring_list)