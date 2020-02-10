customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

data = input("Phone: ")
string = ""

for x in data:
    string += numbers.get(x, f"'{x}' is not in dictionary!") + " "
print(string)
