poem = ("first line\nsecond line")
print("poem")
eneida = """

Встала весна, чорну землю
Сонну розбудила,
Уквітчала її рястом,
Барвінком укрила;
І на полі жайворонок,
Соловейко в гаї
Землю, убрану весною,
Вранці зустрічають…"""

print(eneida)
Save = "☔"
print(Save)
Upp = "Alex"
Upper = "Baron"
FullUPP = Upp + Upper
print(FullUPP)



first_name = 'Donald'
# print(id(first_name))
second_name = 'Trump'
island = "Ormuz"
ukraine = 'Україна'

# fullname = first_name + " " + second_name
fullname = f"{first_name} {second_name}"

# fullname = first_name + " " + second_name + "!!!" + " Hello on "
welcome_message = f"{fullname}!!! Hello on {island}!!!"
print(welcome_message)

# Використовуємо f""" для багаторядкового рядка, щоб змінні працювали
LETTER = f"""
============================================================
           Hello, Mr. {fullname}!
Nice to see you here - on our island {island}!!!

kind regards
============================================================
"""

letter = LETTER
print(letter)

print(id(LETTER))
print(id(letter))