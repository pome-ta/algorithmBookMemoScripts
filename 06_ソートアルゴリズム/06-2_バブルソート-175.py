# バブルソート(単純交換法)で整列する


def bubble_sort(_array: list) -> list:
    array_len = len(_array) - 1
    for near in range(array_len):
        for far in range(array_len, near, -1):
            if _array[far] < _array[far - 1]:
                _tmp = _array[far]
                _array[far] = _array[far - 1]
                _array[far - 1] = _tmp
    return _array


if __name__ == '__main__':
    a: list = [10, 3, 1, 4, 2]
    print(bubble_sort(a))
