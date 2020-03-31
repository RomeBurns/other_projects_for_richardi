def sieve(max):
    primes = [2]
    max = int(max)
    for i in range(2, max):
        for j in range(len(primes)):
            if i % primes[j] == 0:
                break
            if primes[j] == primes[-1]:
                primes.append(i)
    return primes

reason = 600851475143
count = 0
num = 2
while num != reason:
    if reason % num == 0:
        reason = reason / num
    else:
        num += 1
print(num)