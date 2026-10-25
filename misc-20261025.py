# small utilities, no deps

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

if __name__ == "__main__":
    print(most_common("abracadabra"))
