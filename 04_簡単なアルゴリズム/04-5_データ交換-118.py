# データの交換


def switch_var(x: int, y: int) -> tuple:
    _ = x
    x = y
    y = _
    return x, y


if __name__ == '__main__':
    _a: int = 10
    _b: int = 20
    a, b = switch_var(_a, _b)
    print(f'_a={_a}, _b={_b}, a={a}, b={b}')
