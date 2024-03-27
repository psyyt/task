#pritn odd numbers
i = 1
while i <= 10:
    if i % 2 == 1:
        print(i)
    i +=1

#make the multiple table
value = int(input('input the value: '))

x = range(1, 11)
for n in x:
    result = value * n
    print(f"{value} * {n} = {result} ")