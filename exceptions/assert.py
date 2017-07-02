def TestCase(a, b):
    assert a < b, " a is greater than b"
try:
    TestCase(2, 1)
except AssertionError as e:
    print(e)