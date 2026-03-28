def convert_datetime(dt_str: str) -> None:
    """
    Convert a datetime to 12-hour format
    """
    try:
        date_part, time_part = dt_str.strip().split()
        m, d, y = map(int, date_part.split('/'))
        h, mn, s = map(int, time_part.split(':'))

        period = "AM" if h < 12 else "PM"
        h12 = 12 if h % 12 == 0 else h % 12

        print(f"{d:02d}.{m:02d}.{y % 100:02d} {h12:02d}:{mn:02d}:{s:02d} {period}")

    except (ValueError):
        print("Ошибка: неверный формат или значения")
