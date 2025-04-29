
odd_nums = []

for i in range (4655,8712):
    if i%2 != 0:
        odd_nums.append(i)

print(sum(odd_nums))