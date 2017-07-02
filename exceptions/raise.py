def RaiseException(a):
    if type(a) != type('a'):
        raise ValueError("This is not a string")
try:
    RaiseException(3)
except ValueError as e:
    print(e)