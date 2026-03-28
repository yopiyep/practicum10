def bm_find(s, sub, start=0, end=None, all_=False):
    end = len(s) if end is None else min(end, len(s))
    start = max(0, start)

    if sub == "":
        return ",".join(map(str, range(start, end + 1))) if all_ else start

    m = len(sub)
    if m > end - start:
        return "" if all_ else -1

    bad = {c: i for i, c in enumerate(sub)}
    res = []
    i = start

    while i <= end - m:
        j = m - 1
        while j >= 0 and s[i + j] == sub[j]:
            j -= 1

        if j < 0:
            if not all_:
                return i
            res.append(str(i))
            i += 1
        else:
            i += max(1, j - bad.get(s[i + j], -1))

    return ",".join(res) if all_ else -1