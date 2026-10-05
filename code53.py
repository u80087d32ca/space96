# small utilities, no deps

def clamp(value, low, high):
    return max(low, min(value, high))

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

if __name__ == "__main__":
    print(list(chunks(range(22), 10)))
