def print_primes():
    N = int(input("N: "))
    for num in range(2, N + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")