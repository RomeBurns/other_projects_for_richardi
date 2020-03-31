i = 999
j = 999
ans = 0
# true = False
# while j > 0:
#     it = 0
#     num = str(i * j)
#     for i in range(round((len(num)) / 2.0)):
#         jt = (it + 1) * (-1)
#         if num[it] == num[jt]:
#             it += 1
#             true = True
#         else:
#             true = False
#             break
#     if true == True and int(num) > int(ans):
#         ans = num
#         print(ans)
#     if i > 0:
#         i = i - 1
#     else:
#         j = j - 1
#         i = 999

lit = []
while j > 0:
    lit.append(i * j)
    if i > 0:
        i = i - 1
    else:
        j = j - 1
        i = 999
lit.sort(reverse = True)
for i in range(len(lit)):
    lit[i] = str(lit[i])
cool = True
count = 0
while count != len(lit):
    cool = True
    for i in range(round((len(str(lit[count]))) / 2.0)):
        if lit[count][i] != lit[count][(i + 1) * (-1)]:
            cool = False
            break
    count = count - 1
    if cool == True:
        print(lit[count])