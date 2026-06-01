from pprint import pprint

# admin_login = 'admin'
# admin_password = '123'
# admin_salary = 5222
# admin_hobbies = ['tennis', 'soccer']
# is_married = True

# CREATE
admin_data = {
    "login": 'admin3232323',
    "password": '123',
    "salary": 5222,
    "hobbies": ['tennis', 'soccer'],
    'is_married': True,
    "address": {
        'city': 'Lviv',
        'street': "Soborna",
        'building': 15,
        # 'apartment': 56
    },
    'pet_name': None,
}
# print(admin_data)
pprint(admin_data)

# READ
admin_login = admin_data["login"]
print(admin_login)
admin_city = admin_data["address"]['city']
print(admin_city)

# apartment = admin_data["address"]['apartment']
# print(apartment)

admin_address = admin_data["address"]
print(admin_address)

# apartment = admin_address.get('apartment')
apartment = admin_address.get('apartment', 'N/A')
print(apartment)

salary = admin_data["salary"]
print(salary)