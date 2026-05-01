apples = '5'
pears = '2'
# print(type(apples))
apples = int(apples)
pears = int(pears)
# print(type(apples))

total_fruits = apples + pears
# print(total_fruits)

integer_number = 1230000000
integer_number2 = 2_230_000_000
# print(integer_number2)
summa = integer_number + integer_number2
# print(summa)

# -----------------------------------------------------------
# BANANA_PRICE = 65
# banana_quantity = input("Enter banana quantity (integer number) >>> ").strip()
# is_banana_quantity_digit = banana_quantity.isdigit()
#
# if is_banana_quantity_digit:
#     banana_quantity = int(banana_quantity)
#     banana_cost = banana_quantity * BANANA_PRICE
#     banana_order_message = f"{banana_cost=}"
#     print(banana_order_message)
# else:
#     print('Not a valid number')
#
# -----------------------------------------------------------

not_integer_number = 5.32
float_number1 = 655.3156
float_number2 = 0.2
float_number_summa = float_number1 + float_number2
print(float_number_summa)
float_number_summa = round(float_number_summa, 2)
print(float_number_summa)

diff = float_number_summa - 5
print(diff)

mult1 = 5 * 6
print(mult1)

mult2 = 1.0 * 145
print(mult2)

fraction = 5 / 1
print(fraction)

whole_part = 10 // 3
print(whole_part)
rest = 10 % 3
print(rest)

power = 4 ** 2
print(power)

chain = 2 + 6 + 7 - (5 + 56) * 5
print(chain)

apples = 5
pears = 4
if apples == pears:
    print('pears = apples')