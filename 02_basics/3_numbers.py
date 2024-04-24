import math
from decimal import Decimal

x = 234
y = 3
z = 4

print(x + y)

print(x ** y)

print(40 + 2.23)

# print("ali" + 2.23)

# print(40 + 2.23) should be
print(40 + int(2.23))


print(x, y, z) #becoming tuple
print(x + 1, y + 1, z) #becoming tuple
print(2 ** 1000)

result = 1/3.0

print(result)

print(math.floor(-3.5))

print(2 + 1j)

print(0.1 + 0.2)

print(Decimal('0.1') + Decimal('0.2'))

setone = {1, 2, 3, 4}

print(setone & {1,3})

print(setone | {1,3})


print(type(0.1))
print(type(True))
print(type(3))
print(type("0.1"))
print(type({}))
print(type(()))
print(type([]))