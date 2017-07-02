# def function():
#     print('First function')
# function()

# def returning():
#     return 'Second function'
# result = returning()
# print(result)

# def multival():
#     return "One value", 2
# print(multival())

# def add(a, b):
#     return a + b
# result = add(1, 2)
# print(result)

# def default_param(a, b = 4, c = 5):
#     return a + b + c
# result = default_param(1)
# print(result)

# def outer_function(a):
#     def nested_function(b):
#         return b * a
#     a = nested_function(a)
#     return a
# print(outer_function(4))

# def f(a):
#     def g(b):
#         def h(c):
#             return a * b * c
#         return h
#     return g
# print(f(1)(2)(3))

## RECURSION
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n - 1)
# print(sum(10))

# def tail_sum(n, accumulator = 0):
#     if n == 0:
#         return accumulator
#     else:
#         return tail_sum(n - 1, accumulator + n)
# print(tail_sum(10))