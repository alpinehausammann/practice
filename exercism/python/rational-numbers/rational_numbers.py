from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
    	numer = (self.numer * other.denom) + (other.numer * self.denom)
    	denom = self.denom * other.denom
    	numer, denum = self.negative_check(numer, denum)
    	return Rational(numer, denom)

    def __sub__(self, other):
    	numer = (self.numer * other.denom) - (other.numer * self.denom)
    	denom = self.denom * other.denom
    	numer, denum = self.negative_check(numer, denum)
    	return Rational(numer, denom)

    def __mul__(self, other):
    	numer = self.numer * other.numer
    	denum = self.denom * other.denom
    	numer, denom = self.negative_check(numer, denum)
    	return Rational(numer, denom)

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
    	
        pass
        
    def negative_check(self, numer, denum):
        if numer < 0 and denum < 0:
        	numer = numer * -1
        	denum = denum * -1
        	
        return numer, denum
        	
if __name__ == "__main__":
	x = Rational(1,2) * Rational(2,3)
	print(x)
