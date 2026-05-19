from letter import LETTER_TEMPLATE

client_name = input("Введіть ім'я та прізвище: ")
trip_date = input("Введіть дату поїздки: ")
num_persons = int(input("Введіть кількість осіб: "))

PRICE_PER_PERSON = 15000

total = num_persons * PRICE_PER_PERSON

if num_persons > 5:
    discount_amount = total * 0.05
else:
    discount_amount = 0

final_total = total - discount_amount

print(LETTER_TEMPLATE.format(
    name=client_name,
    date=trip_date,
    persons=num_persons,
    price_per_person=PRICE_PER_PERSON,
    total_price=total,
    discount=discount_amount,
    final_price=final_total
))