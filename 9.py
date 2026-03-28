def seconds_since_new_year(dt_str):
    try:
        date, time = dt_str.strip().split()
        m, d, y = map(int, date.split('/'))
        h, mn, s = map(int, time.split(':'))
        days_in_month = [31, 29 if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31,
                         30, 31]

        seconds = (sum(days_in_month[:m - 1]) + d - 1) * 86400 + h * 3600 + mn * 60 + s
        return seconds

    except:
        print("Ошибка")
        return None