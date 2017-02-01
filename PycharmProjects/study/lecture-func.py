n = 10
def fuc(n):
    n = n*10
fuc(10)
print(n)

def fuc2():
    global n
    n = n*10
fuc2()
print(n)

def noDefRngParam(*n):
    for e in n:
        print('val={}'.format(e))
noDefRngParam(1,2,3,4,5,6,7,8,9)

def noDefRngParam2(a,*n):
    for e in n:
        print('name={} , val={}'.format(a,e))
noDefRngParam2('karoscha','a','b','c','d','e','f')