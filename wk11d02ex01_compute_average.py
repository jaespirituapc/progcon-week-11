numbers = [0] * (4)

numbers[0] = 22
numbers[1] = 9
numbers[2] = 0
numbers[3] = 17
total = 0
count = 0
index = 0
while index < len(numbers) and numbers[index] != 0:
    total = total + numbers[index]
    count = count + 1
    index = index + 1
if count > 0:
    print(float(total) / count)
else:
    print(0)
