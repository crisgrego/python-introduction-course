# class Complex:
#     'Simulates complex numbers' # doc string (short description of the class itself)
#     def __init__(self, real, imag):  # constructor
#         self.real = real
#         self.imag = imag

# c = Complex(1, 2) 
# print(c.real, c.imag)

## DEFAULT PARAMETERS
# class Complex:
#     'Simulates complex numbers' 
#     def __init__(self, real = 0, imag = 0):
#         self.real = real
#         self.imag = imag

# c = Complex() 
# print(c.real, c.imag)

## Define restrictions
# class Complex:
#     'Simulates complex numbers' 
#     def __init__(self, real = 0, imag = 0):
#         if type(real) not in (int, float) or type(imag) not in (int, float):
#             raise Exception('Args are notnumbers!')
#         self.real = real
#         self.imag = imag

# c = Complex() 
# print(c.real, c.imag)