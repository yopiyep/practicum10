def calculate_final_price(price: float, has_discount_card: bool, is_holiday: bool) -> float:
    max_discount = 15
    total_discount = 0


    if price > 30000:
        total_discount += 10
    elif price > 20000:
        total_discount += 7
    elif price > 15000:
        total_discount += 5
    elif price > 5000:
        total_discount += 3
    if has_discount_card:
        total_discount += 5
    if is_holiday:
        total_discount += 3
    final_discount = min(total_discount, max_discount)
    final_price = price * (1 - final_discount / 100)

    return round(final_price, 2)