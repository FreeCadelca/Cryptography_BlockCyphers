import numpy
from IntMod import IntMod

a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[3, 2], [1, 4]])
c = a.dot(b)
a_rev = numpy.linalg.inv(a)
print(a_rev)

