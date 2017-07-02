## Tuple
# tup = (1, 'abc', 2, 'cde')
# tup1 = 3, 'efg', True
# tup3 = ('A', )
# print(tup) # full tuple
# print(tup[0]) # one element
# print(tup[0:2]) # only two first elements

# # Tuple does not support item assignment
# tup = (1, 'abc', 2, 'cde')
# try:
#     tup[3] = 5
# except Exception as e:
#     print(e)

## Operators
# tup = (1, 'abc', 2, 'cde')
# tup = tup[0:3] + (5,) # Adding tuples
# (1, 2, 3) == (1,2) # False
# print(tup)
# print(5 in tup) # Check if tuple contains some value

## Iterate
# for element in ('a', 'b', 'c'):
#     print(element)

## Tuples for multiple results
# def giveme_multiple_results():
#     return (1, 2, 'a')
# print(giveme_multiple_results())

## Tuples functions
# tup = (2, 5, 1)
# print(len(tup)) # Number of elements in the tuple
# print(max(tup)) # Element with highest value in the tuple
# print(min(tup)) # Element with lowest value in the tuple