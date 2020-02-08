names = ["John", "Bob", "Mosh", "Sarah", 'Mason']
print(names[0])     #index -1 is last element
names[0] = 'Jon'
print(names[2:4])
print(names[2:])

#Find largest number in list
numbers = [4, 9, 8, 12, 3, 1, 5]
max = numbers[0]
for x in numbers:
    if x > max:
        largest = x
print(max)

#2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][2] = 20
print(matrix[0][1])
print(matrix[0][2])

for row in matrix:
    print()
    for item in row:
        print(item)

numbers = [5, 2, 1, 3, 7, 4, 3]
numbers.append(20)      #add at end
numbers.insert(0, 10)   #insert to index position
#numbers.remove(5)
print(numbers)
print(numbers.index(20))
print(numbers.count(3))
numbers.sort()
print(numbers)
numbers_sorted = numbers.copy()
print(numbers_sorted)
numbers.pop()           #pop out last index
numbers.clear()         #empty list

#remove duplicates in list
remove_duplicates = [4, 5, 2, 1, 5, 3, 2, 5, 6, 4, 5]
uniques = []
for number in remove_duplicates:
    if number not in uniques:
        uniques.append(number)
print(uniques)