user_dict = {}

num_books = int(input("Enter the number of books you want to add: "))

for i in range(num_books):
    name_books = input("Enter name of book: ")
    price = int(input("Enter value of book: "))  # Convert price to int for numerical operations
    user_dict[name_books] = price

print("Dictionary after adding user input:", user_dict)

# Remove duplicates based on price
temp = []
res = {}

for name_books, price in user_dict.items():
    if price not in temp:
        temp.append(price)
        res[name_books] = price

print("The list after removing duplicate books:", res)

# Sort prices in ascending order
sorted_prices = sorted(user_dict.items(), key=lambda x: x[1])
print("Books sorted by price in ascending order:", sorted_prices)

# Sort book names in descending order
sorted_books_desc = sorted(user_dict.items(), key=lambda x: x[0], reverse=True)
print("Books sorted by name in descending order:", sorted_books_desc)

# Filter books based on price (> 500 and <= 500)
books_above_500 = {name: price for name, price in user_dict.items() if price > 500}
books_below_equal_500 = {name: price for name, price in user_dict.items() if price <= 500}

print("Books with price greater than 500:", books_above_500)
print("Books with price less than or equal to 500:", books_below_equal_500)
