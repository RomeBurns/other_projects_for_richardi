squaresumm = 0
summsquare = 0
for i in range(101):
    squaresumm = squaresumm + i
squaresumm = squaresumm * squaresumm

for i in range(101):
    summsquare = summsquare + ( i * i )
print(summsquare)
print(squaresumm)
print(summsquare - squaresumm)