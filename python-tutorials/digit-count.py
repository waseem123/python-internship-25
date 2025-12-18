n = 145565656526356323232
temp = n
count = 0

while n!=0:
    count =  count + 1
    n = n // 10

print(f'THERE ARE {count} digits in {temp}')