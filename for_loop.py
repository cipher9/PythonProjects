price = [10, 20, 30]
cost = 0
for item in price:
    cost += item
print(f"Total: {cost}")

# matrix
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]
for x in range(len(numbers)):
    print("x" * numbers[x])