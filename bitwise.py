x = 8
y = 1

a = x & y
b = x | y
c = x >> y
d = x << y

e = y & x
f = y | x
g = y >> x
h = y << x

print(f'binary values of x and y are {bin(x)} {bin(y)}')

print(f'the result of x & y is {a}')
print(f'the result of x | y is {b}')
print(f'the result of x >> y is {c}')
print(f'the result of x << y is {d}')

print(f'the result of y & x is {e}')
print(f'the result of y | x is {f}')
print(f'the result of y >> x is {g}')
print(f'the result of y << x is {h}')