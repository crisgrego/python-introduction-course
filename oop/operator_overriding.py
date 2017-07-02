import math as m

class Complex:
    'Simulates complex numbers' 
    def __init__(self, real = 0, imag = 0):
        self.set_imag(imag)
        self.set_real(real)
        
    def get_real(self):
        return self.__real

    def get_imag(self):
        return self.__imag

    def set_real(self, val):
        if type(val) not in (int, float):
            raise Exception('Real part must be a number')
        self.__real = val

    def set_imag(self, val):
        if type(val) not in (int, float):
            raise Exception('Real part must be a number')
        self.__imag = val

    def __str__(self): ## to string operator
        return str(self.get_real()) + '+' + str(self.get_imag()) + 'i'

    def __add__(self, other): ## + operator
        return Complex(self.get_real() + other.get_real(), self.get_imag() + other.get_imag())
    
    def __mul__(self, other): ## * operator
        if type(other) in (int, float):
            return Complex(self.get_real() * other, self.get_imag() * other)
        else:
            return Complex(self.get_real() * other.get_real() - self.get_imag() * other.get_imag(),
                           self.get_imag() * other.get_imag() + self.get_real() * other.get_real())
    
    def __truediv__(self, other):
        if type(other) in (int, float):
            return Complex(self.get_real() / float(other), self.get_imag() / float(other))
        else:
            a, b, c, d = self.get_real(), self.get_imag(), other.get_real(), other.get_imag()
            nomminator = c * c + d * d
            return Complex((a * c + b * d) / nomminator, (b * c - a * d)/ nomminator)

a = Complex(5, 0.3)
b = Complex(-3, 4)

print(a + b)
print(a * b)
print(a / b)
print(b / 2)