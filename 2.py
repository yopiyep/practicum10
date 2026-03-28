n = int(input())


def fibanachi(n: int) -> None:
    x = [1, 1]
    for i in range(n - 2):
        x.append(x[i] + x[i + 1])
    print(x)
fibanachi(n)