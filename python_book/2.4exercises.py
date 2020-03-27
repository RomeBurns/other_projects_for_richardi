print(((3+7)//2%2)**3)

#(x-2)**3+3*x

x = 40

x = 0.5

hold = x
for i in range(3):
    x *= hold
x *= x
x *= x

'+++++'

def triangle(s):
    if len(s) != 1:
        return 0
    print(s,s,s,s,s)
    n = ' '
    print(n,s,s,s,n)
    print(n,n,s,n,n)

#The returned value is what is in the print functions. This function does not need to return something to a larger function, as it is only meant to print.

def triangle2(s):
    if len(s) != 1:
        return 0
    m = ' '
    print(s,s,s,s,s, '\n', m,s,s,s,m, '\n', m,m,s,m,m,)

def triangle3(s):
    n = ''
    print(s,s,s,s,s)
    for i in range(len(s)):
        n = n + ' '
    print(n,s,s,s,n)
    print(n,n,s,n,n)