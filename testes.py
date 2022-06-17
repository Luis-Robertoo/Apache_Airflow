def foo():
    print('antes primeiro')
    yield 10
    print('depois primeiro')
    print('antes segundo')
    yield 20
    print('depois segundo')

g = foo()

print(next(g))

print(next(g))

print('-=-'*12)

for x in g:
    print(x)


