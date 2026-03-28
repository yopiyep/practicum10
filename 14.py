def find_all(s: str, sub: str):
    res = []
    n, m = len(s), len(sub)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            res.append(str(i))

    return ",".join(res)
