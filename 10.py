def print_valid_numbers(A, B):
    if A > B:
        A, B = B, A

    valid_digits = {'1', '3', '4', '8', '9'}

    for num in range(A, B + 1):
        if all(digit in valid_digits for digit in str(num)):
            print(num, end=" ")
