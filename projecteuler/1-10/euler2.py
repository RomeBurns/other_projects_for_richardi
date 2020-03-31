fib = [1,2,3,5,8]
while fib[-1] <= 4000000:
    fib.append(fib[-1] + fib[-2])
ans = 0
for i in range(len(fib)):
    if fib[i] % 2 == 0:
        ans += fib[i]
print(ans)