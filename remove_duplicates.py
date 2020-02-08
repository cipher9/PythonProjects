#remove duplicates in list
remove_duplicates = [4, 5, 2, 1, 5, 3, 2, 5, 6, 4, 5]
uniques = []
for number in remove_duplicates:
    if number not in uniques:
        uniques.append(number)
print(uniques)