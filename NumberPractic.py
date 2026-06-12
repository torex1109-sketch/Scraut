print("Введіть, скільки грошей у кожного друга:")
groschi_1 = int(input("Друг 1: "))
groschi_2 = int(input("Друг 2: "))
groschi_3 = int(input("Друг 3: "))
groschi_4 = int(input("Друг 4: "))

vsi_hroschi = groschi_1 + groschi_2 + groschi_3 + groschi_4

pizza = 250
cola = 40
sous = 25

kilkist_pizz = vsi_hroschi // pizza
zalishok = vsi_hroschi % pizza

kilkist_cola = zalishok // cola
zalishok = zalishok % cola

kilkist_sous = zalishok // sous
vash_zdacha = zalishok % sous

print("---")
print(f"Загальний бюджет: {vsi_hroschi} грн")
print(f"Ви можете купити:")
print(f"- Піца: {kilkist_pizz} шт.")
print(f"- Кола: {kilkist_cola} шт.")
print(f"- Соус: {kilkist_sous} шт.")
print(f"Решта залишиться: {vash_zdacha} грн")