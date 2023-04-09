sum = 0
a = 1
while a != 0:
    a = int(input())
    if a >= 100 and a < 1000 and a % 4 == 0:
        sum += 1
print(sum)
