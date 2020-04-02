#subsets of t: {a,b} {a} {b} {None}

# set of two elements: 4, set of three elements: 8, set of four elements: 16 set of n elements: 2^n
# work: {a,b,c} {none} {a} {b} {c} {ab} {ac} {bc}

def problem3():
    domain = [1,2,3,4,5]
    rangee = []
    if len(domain) == 5:
        for i in range(1-6):
            if i in domain == False:
                return 0
            rangee.append(domain[i - 1] + 3)

def problem4():
    domain = [-1,1,2]
    rnage = []
    for i in range(len(domain)):
        domain[i] = domain[i] ** 2
    rnage = domain

#A function cannot have a larger range than domain. The largest a domain can be is when the function is one to one and each element of the range can be accessed by onlymone element of the domain. A function can only produce one element of range for each element of domain
import math
def problem6():
    domain = []
    rnage = set()
    for j in range(len(domain)):
        rnage.add(math.sqrt(domain[j] / abs(domain[j])))
# zero will produce zero, positive values will produce one, and negative values will produce i for imaginary number, where i^2 = -1

#an infinite number of functions can be defined. One example of a type of function with infinite possibilities alone would be to increment each element of the domain by increasing incrments

def problem8():
    domain = []
    rnage = set()
    for i in range(len(domain)):
        if domain[i] % 2 == 0:
            domain[i] += 1
        rnage.add(domain[i])

def problem10(s):
    domain = s
    if domain <= 1 and domain > 0:
        return domain + 1

# 9, 5 and this is the case because a set does not have multiple copies of the same number

