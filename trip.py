import math
from pywebio.input import input_group, select, slider
from pywebio.output import put_error, put_text

data = input_group("Організація поїздки", [
    slider("Учні", name="students", min_value=0, max_value=100),
    slider("Вчителі", name="teachers", min_value=1, max_value=10),
    select("Транспорт", name="transport", options=["Автобус", "Поїзд"]),
    slider("Дні", name="days", min_value=0, max_value=14)
])

students = data["students"]
teachers = data["teachers"]
transport = data["transport"]
days = data["days"]

if students == 0:
    put_error("Помилка: учнів не може бути 0")
else:

    total_people = students + teachers

    if transport == "Автобус":
        buses = math.ceil(total_people / 40)
        transport_cost = buses * 5000
    else:
        buses = 0
        transport_cost = total_people * 300

    nights = days - 1 if days > 0 else 0
    hotel_cost = total_people * 400 * nights

    total = transport_cost + hotel_cost

    if total_people > 30:
        total = total * 0.90

    put_text(f"Всього людей: {total_people}")
    if buses > 0:
        put_text(f"Потрібно автобусів: {buses}")
    put_text(f"Транспорт: {transport_cost} грн")
    put_text(f"Проживання: {hotel_cost} грн")
    put_text(f"Разом до сплати: {total} грн")