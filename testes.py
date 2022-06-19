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





entrada = 5
c = 1
t1 = 0
t2 = 1

while c < entrada:
    t3 = t1 + t2
    #print(" > ", t3, end=" ")
    t1 = t2
    t2 = t3
    c+=1
print(t3)


print('\n','-='*9)
def fin(n):

    if(n in [0, 1]):
        return n
    return fin(n - 1) + fin(n - 2)


print(fin(entrada))

print('=-='*4)




