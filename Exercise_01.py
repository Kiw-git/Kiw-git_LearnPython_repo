# out put should looks like this
# 2
# 4
# 6
# 8
# We have 4 even numbers

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")
