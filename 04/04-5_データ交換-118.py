# データの交換


def switch_var(a: int, b: int) -> tuple:
    _ = a
    b = a
    a = _
    return a, b


if __name__ == '__main__':
    _a: int = 10
    _b: int = 20
    a, b = switch_var(_a, _b)
    print(a, b)

