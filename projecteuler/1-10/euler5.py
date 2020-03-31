divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
nums = 1
count = 0
for i in range(len(divisors)):
    nums = nums * divisors[i]
print(nums)


while count < 19:
    potential = nums
    cool = 0
    if potential % divisors[count] == 0:
        potential = potential / divisors[count]
        while cool < 19 and potential % divisors[cool] == 0:
            cool += 1
        if cool == 19:
            nums = potential
            print("this")
        else:
            count += 1
print(nums)