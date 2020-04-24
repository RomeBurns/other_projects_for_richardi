def problem1(a, b):
    return ((a + b)/2)

# nothing is different, as the new value wasn't returned or declared as global variables.

from math import sqrt
def problem3(a, b, c):
    if (b**2-4*a*c) < 0:
        return None
    hold = sqrt(b**2-4*a*c)
    ans = (-1 * b + hold) / (2 * a)
    ans0 = (-1 * b - hold) / (2 * a)
    return ans, ans0
a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
this = problem3(a, b, c)
if this == None:
    print('no solutions in real numbers')

# error, followed by 0

def print_n_times(n, obj='*'):
    print(n*str(obj))
# one argument is missing, but now it's not

