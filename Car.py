car = {
    "model": "Toyota RAV4 Hybrid",
    "price": 1450000,
    "engine_volume": 2.5,
    "full_weight": 2225,
    "max_speed": 180,
    "fuel_consumption": 4.8,
    "interior_features": [
        "Мультимедіа 10.5 дюймів",
        "Цифрова панель приладів",
        "Клімат-контроль"
    ],
    "luggage_compartment": {
        "regular_volume": 580,
        "folded_volume": 1690
    }
}

car["max_trailer_weight"] = 1500

print(f"Назва авто: {car['model']}")
print(f"Ціна: {car['price']} грн")
print(f"Перша опція інтер'єру: {car['interior_features'][0]}")
print(f"Об'єм зі складеними сидіннями: {car['luggage_compartment']['folded_volume']} л")

car["insurance_payment"] = car["price"] * 0.005
print(f"Страховий платіж: {car['insurance_payment']} грн")

trip_cost = car["fuel_consumption"] * 2 * 93
print(f"Вартість мандрівки на 200 км: {trip_cost} грн")