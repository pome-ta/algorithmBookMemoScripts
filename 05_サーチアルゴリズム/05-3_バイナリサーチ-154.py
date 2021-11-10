# バイナリサーチ(二分探索法)で探索する


def binary_search(_array: list, search: int) -> int:
    array_len: int = len(_array)
    # todo: 初期値はエラーの値(-1)
    find_id: int = -1
    left: int = 0
    right: int = array_len - 1
    for _ in range(array_len):
        middle: int = int((left + right) / 2)
        if search == _array[middle]:
            find_id = middle
            break
        elif search > _array[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return find_id


if __name__ == '__main__':
    # todo: 昇順のlist
    a: list = [1, 2, 4, 5, 10]
    search_value: int = 4
    print(f'バイナリサーチ: {binary_search(a, search_value)}')
