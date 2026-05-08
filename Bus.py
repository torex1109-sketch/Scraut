from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
import math


def trip_calculator():
    put_markdown("# Калькулятор шкільної поїздки")

    students = input("Скільки учнів?", type=NUMBER)

    if students == 0:
        put_error("Помилка: Потрібен хоча б один учень!")
        return

    teachers = input("Скільки вчителів?", type=NUMBER)
    transport = select("Транспорт", ["Автобус", "Поїзд"])
    days = slider("Скільки днів?", min_value=0, max_value=10)

    total_people = students + teachers

    if transport == "Автобус":
        count_bus = math.ceil(total_people / 40)
        transport_price = count_bus * 5000
    else:
        count_bus = 0
        transport_price = total_people * 300

    if days > 0:
        hotel_price = total_people * 400 * (days - 1)
    else:
        hotel_price = 0

    total_sum = transport_price + hotel_price

    if total_people > 30:
        total_sum = total_sum * 0.9

    put_markdown("### Підсумок:")
    put_text(f"Всього людей: {total_people}")

    if transport == "Автобус":
        put_text(f"Потрібно автобусів: {count_bus}")

    put_text(f"Вартість транспорту: {transport_price} грн")
    put_text(f"Вартість проживання: {hotel_price} грн")

    put_markdown(f"## **Разом до сплати: {total_sum} грн**")


start_server(trip_calculator, port=8080)