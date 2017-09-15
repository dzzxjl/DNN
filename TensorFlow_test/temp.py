from numpy.random import RandomState

rdm = RandomState(1)

print(type(rdm))
print(rdm)

X = rdm.rand(128, 2)

print(type(X))
print(X)

Y = [ [int(x1+x2 < 1)] for (x1, x2) in X]

print(Y)