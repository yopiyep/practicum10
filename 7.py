def print_common_multiples(A: int, B: int, N: int) -> None:
    start = max(A, B)
    found = False

    for num in range(start, N + 1):
        if num % A == 0 and num % B == 0:
            print(num, end=" ")
            found = True

    if not found:
        print("Нет общих кратных, не превосходящих N")