class Complex(object):
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

    real = property(get_real,set_real)
    imag = property(get_imag, set_imag)