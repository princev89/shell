set1 = {0, 2, 4, 6, 8}
set2 = {1, 2, 3, 4, 5}

count = 0

for i in set2:
    if i in set1:
        count += 1
print(count)
