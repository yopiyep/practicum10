def make_payment(P: float) -> None:
    if 20 <= P <= 1000:
        print('Успех')
    else:
        print('Повторить попытку')