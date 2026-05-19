# print("dfjkgb"     '111111')
# CRUD

# Create

cities_string = "Odesa ++ Lviv ++ Krakiv ++ Kyiv"
# cities_list = cities_string.split()
cities_list = cities_string.split('++')
print(cities_list)

empty_list = []

numbers = [1, 5, 6, 5.6]

products = [
    'milk',
    'bread',
    'salt',
]

print(products)

mixed = [...]


# Read
# get by index
first_product = products[0]
print(first_product)
second_product = products[1]

products_quantity = len(products)
print(products_quantity)

element_wanted = 3
element_wanted_index = element_wanted - 1

if products_quantity >= element_wanted:
    wanted_product = products[element_wanted_index]
    print(wanted_product)

last_product = products[-1]
print(last_product)
first_product_back = products[-4]
print(first_product_back)

# for each

print("*" * 50)
total_product_words_length = 0
words_chain = ''

for product in products: ...

print(total_product_words_length)
print(words_chain)
print(55555555555555555555555555)

# Update
# change elem
products[-1] = 'apples'
print(products)
