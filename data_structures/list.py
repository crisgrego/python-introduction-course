import functools

# list1 = [1, 'abc', (2, 3)]
# print(list1)
# print(list1[0])
# print(list1[0:2])
# print(list1 + ['4'])
# print(list1 * 2)
# print(2 in list1)
# print(list1 == [1, 'abc', (2, 3)])

# list2 = [1, 2, 3]
# list2.append(6)
# list2[len(list2):] = [7] # Is the same as append
# print(list2)

## functions

## map(lambda, secuence) and returns a map opject
# print(list(map(lambda x: x**2 + 3*x + 1, [1,2,3,4]))) # use the map opbject created by map to show a list

# filter(lambda, secuence) and returns a map obejct
# print(list(filter(lambda x: x < 4, [1,3,4,5,6])))

# reduce(lambda, secuence) and returns a map object
# a module is needed to use this function
print(list(functools.reduce(lambda x, y: x * y, [1,2,3,4])))