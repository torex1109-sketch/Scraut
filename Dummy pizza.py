import requests

url = "https://dummyjson.com/recipes"
response = requests.get(url)
data = response.json()
recipes = data["recipes"]

pizza_list = []
italian_count = 0
max_calories = 0
max_caloric_name = ""
degrees_190_list = []
total_reviews = 0

for recipe in recipes:
    name = recipe["name"]

    if "pizza" in name.lower():
        pizza_list.append(name)

    if recipe["cuisine"] == "Italian":
        italian_count = italian_count + 1

    calories = recipe["caloriesPerServing"]
    if calories > max_calories:
        max_calories = calories
        max_caloric_name = name

    instructions = recipe["instructions"]
    if len(instructions) > 0:
        first_step = instructions[0]
        if "190" in first_step:
            degrees_190_list.append(name)

    total_reviews = total_reviews + recipe["reviewCount"]

print("1. Список піц:", pizza_list)
print("2. Кількість італійських страв:", italian_count)
print(f"3. Найкалорійніша страва: {max_caloric_name} ({max_calories} калорій)")
print("4. Готуються при 190°C:", degrees_190_list)
print("5. Всього переглядів:", total_reviews)