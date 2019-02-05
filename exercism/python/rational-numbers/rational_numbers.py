from __future__ import division


class Rational(object):
  def __init__(self, numer, denom):
    self.numer = numer
    self.denom = denom
    self.numer, self.denom = self.gcd(self.numer,self.denom)

  def __eq__(self, other):
    return self.numer == other.numer and self.denom == other.denom

  def __repr__(self):
    return '{}/{}'.format(self.numer, self.denom)

  def __add__(self, other):
    numer = (self.numer * other.denom) + (other.numer * self.denom)
    denom = self.denom * other.denom
    numer, denom = self.negative_check(numer, denom)
    return self.gcd(numer, denom)

  def __sub__(self, other):
    numer = (self.numer * other.denom) - (other.numer * self.denom)
    denom = self.denom * other.denom
    numer, denom = self.negative_check(numer, denom)
    return self.gcd(numer, denom)

  def __mul__(self, other):
    numer = self.numer * other.numer
    denom = self.denom * other.denom
    numer, denom = self.negative_check(numer, denom)
    return self.gcd(numer, denom)

  def __truediv__(self, other):
    numer = self.numer * other.denom
    denom = other.numer * self.denom
    numer, denom = self.negative_check(numer, denom)
    return self.gcd(numer, denom)

  def __abs__(self):
    return self.gcd(self.numer * self.is_negative(self.numer),self.denom * self.is_negative(self.denom))

  def __pow__(self, power):
  	return self.gcd(self.numer**power,self.denom**power)
    

  def __rpow__(self, base):
    return round(base ** (self.numer/self.denom), 8)
    

  def negative_check(self, numer, denom):
    if numer < 0 and denom < 0:
      numer = numer * -1
      denom = denom * -1
    return numer, denom

  def is_negative(self, num):
    if num < 0:
      return -1
    return 1

  def gcd(self, numer, denom):
    negative = (self.is_negative(numer),self.is_negative(denom))
    numer = numer * negative[0]
    denom = denom * negative[1]
    
    if numer == 0 or denom == 0:
      return Rational(0,1)

    if numer < denom:
      for i in range(numer, denom + 1):
        if numer % i == 0 and denom % i == 0:
          numer = (numer * negative[0]) / i
          denom = (denom * negative[1]) / i
    elif numer > denom:
      for i in range(denom, numer + 1):
        if numer % i == 0 and denom % i == 0:
          numer = (numer * negative[0]) / i
          denom = (denom * negative[1]) / i
    else:
      numer = 1
      denom = 1
		
    return Rational(int(numer), int(denom))

if __name__ == "__main__":
  x = Rational(-1,2) ** 9
  print(x)
