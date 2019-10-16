from scipy.stats import chisquare as chi2
ans = 0
summed = []
new = []
iters = int(input("How many iterations do you want to input: "))
dim_o = int(input("dimension of variables: "))
print("all trials must have the same number of test subjects.")
for i in range(dim_o):
    summed.append(0)
for i in range(iters):
    O = []
    E = []
    for i in range(dim_o):
        O.append(int(input("value of next variable: ")))
    for i in range(dim_o):
        E.append(sum(O) / dim_o)
    for i in range(dim_o):
        summed[i] = summed[i] + O[i]
    prob1 = chi2(O, E)
    print(prob1[1])
    for a in range(dim_o):
        new.append(O[a])

for i in range(dim_o):
    summed[i] = summed[i] / iters
for i in range(iters):
    w = []
    for k in range(dim_o):
        w.append(new[0])
        new.pop(0)
    ans = ans + chi2(w, summed)[1]
print(summed)
print(ans / iters)