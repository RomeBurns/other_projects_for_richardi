def pronlem1(a, b):
    ans = a + ' ' + b
    return ans

def print_house():
    print(' /\\\n/  \\\n|  |\n|__|')

def right_justify(s, w):
    while len(s) != w:
        s.append(' ')
    return s

def print_10_dollars():
    print(10 * '$')
# this function multiplies the string $ to create a larger string. the above function prints it while te below function returns it.
def make_10_dollars():
    return (10 * '$')

# chch
# ch
####
###
##

# the first answer is 21, due to the order of operations, and the second answer doesn't return anything, as 0 !> 0.

def read_int():
    return int(input('enter an integer: '))
# neither result produces anything that can be reduced to an integer data type, so it gives an error.

# does not raise exception: b, c, d, e, f, g, h