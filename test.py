data = []

for i in range(1, 10):
    data.append([i])

for i, val in enumerate(data):
    data[0].append([i])


print(data)
