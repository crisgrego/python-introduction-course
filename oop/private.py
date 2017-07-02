import math as m

# To declare properties private we only have to name
# them with 1 or 2 underscores
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
    
    def get_modulus(self):
        return m.sqrt(self.get_real() * self.get_real() + self.get_imag() * self.get_imag())

    def get_phi(self):
        return m.atan2(self.get_imag(), self.get_real())

c = Complex()
c.set_imag(2)
c.set_real(2)
print(c.get_real(), c.get_imag())