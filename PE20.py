ans = 1

for i in range(1,101):
    ans *= i

fin = 0
while ans > 0:
    fin += (ans%10)
    ans /= 10

print fin
