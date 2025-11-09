def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fib(limit):
    if limit < 0:
        return []
    if limit == 0:
        return [0]
    if limit == 1:
        return [0, 1]
    fibs = [0, 1]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > limit:
            break
        fibs.append(next_fib)
    return fibs


def main():
    LIMIT = 2971215073
    fibs = fib(LIMIT)
    primeless_fibs = [num for num in fibs if not is_prime(num)]
    print("\n".join(map(str, primeless_fibs)))


if __name__ == "__main__":
    main()

