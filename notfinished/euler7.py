primes = [2]
maxi = 2
while len(primes) < 10001:
    maxi += 1
    for i in range(2, maxi):
        for j in range(len(primes)):
            if i % primes[j] == 0:
                break
            if primes[j] == primes[-1]:
                primes.append(i)
                print(len(primes))

print(primes[10001])