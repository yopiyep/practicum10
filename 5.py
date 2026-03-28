def calculate_card_value() -> float:
    card_price = float(input("Введите стоимость карты (5, 10, 25, 50 или 100): "))


    if card_price not in [5, 10, 25, 50, 100]:
        print("Ошибка: недопустимая стоимость карты.")
        return None

    if card_price == 25:
        bonus = 3
    elif card_price == 50:
        bonus = 8
    elif card_price == 100:
        bonus = 20
    else:
        bonus = 0

    total_value = card_price + bonus

    return total_value