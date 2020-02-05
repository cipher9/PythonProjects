price = [10, 20, 30]
cost = 0
for item in price:
    cost += item
print(f"Total: {cost}")

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")