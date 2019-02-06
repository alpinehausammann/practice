from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
      if numer == 0 or denom == 0:
        self. numer = 0
        self.denom = 1
      else:
        self.numer, self.denom = self.negative_correction(numer, denom)
        self.numer = int(numer/self.gcd(numer,denom))
        self.denom = int(denom/self.gcd(numer,denom))

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = (self.numer * other.denom) + (other.numer * self.denom)
        denom = self.denom * other.denom
        numer, denom = self.negative_correction(numer, denom)
        return Rational(numer/self.gcd(numer,denom), denom/self.gcd(numer,denom))

    def __sub__(self, other):
        numer = (self.numer * other.denom) - (other.numer * self.denom)
        denom = self.denom * other.denom
        numer, denom = self.negative_correction(numer, denom)
        return Rational(numer/self.gcd(numer, denom), denom/self.gcd(numer, denom))

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        numer, denom = self.negative_correction(numer, denom)
        return Rational(numer/self.gcd(numer, denom), denom/self.gcd(numer, denom))

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = other.numer * self.denom
        numer, denom = self.negative_correction(numer, denom)
        return Rational(numer/self.gcd(numer, denom), denom/self.gcd(numer, denom))

    def __abs__(self):
        numer = self.numer
        denom = self.denom
        if self.is_negative(self.numer):
            numer = numer * -1
        if self.is_negative(self.denom):
            denom = denom * -1
        return Rational(numer, denom)

    def __pow__(self, power):
        numer = self.numer ** power
        denom = self.denom ** power
        common_div = self.gcd(numer, denom)
        return Rational(numer / common_div, denom / common_div)

    def __rpow__(self, base):
        return round(base ** (self.numer / self.denom), 8)

    def is_negative(self, num):
        if num < 0:
            return True
        return False
        
    def negative_correction(self,numer,denom):
        if self.is_negative(numer) and self.is_negative(denom):
          numer = numer * -1
          denom = denom * -1
        if not self.is_negative(numer) and self.is_negative(denom):
          numer = numer * -1
          denom = denom
        return numer, denom

    def gcd(self, numer, denom):
        if numer == 0 or denom == 0:
        	return 1

        if self.is_negative(numer):
            temp_numer = numer * -1
        else:
            temp_numer = numer
        if self.is_negative(denom):
            temp_denom = denom * -1
        else:
            temp_denom = denom

        while temp_numer != temp_denom:
            if temp_numer > temp_denom:
                temp_numer = temp_numer - temp_denom
            if temp_numer < temp_denom:
                temp_denom = temp_denom - temp_numer


        return int(temp_numer)
        
if __name__ == '__main__':
	x =Rational(-1,2) / Rational(-2,3)
	print(x)

