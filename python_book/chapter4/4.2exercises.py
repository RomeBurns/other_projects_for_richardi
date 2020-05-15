# Seive of eratosthenes, any application of pythagoros's theorem

def problem2(s):
    summ = 0
    for i in range(s):
        summ = summ + i
    return (summ + s)

def problem3(m, n):
    n2 = n
    mult = 0
    spare = 0
    while n2 < m:
        if n2 + n < m:
            n2 = n2 + n
            mult += 1
        elif n2 + n == m:
            mult += 1
            return mult, spare
        else:
            spare = m - n2
            return mult, spare

def problem4(s):
    return 3**s