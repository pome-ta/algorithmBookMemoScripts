# リニアサーチ(線形探索法)で探索する


def linear_search(_array: list, search: int) -> int:
    # todo: 初期値はエラーの値(-1)
    find_id: int = -1
    for index, num in enumerate(_array):
        if search == num:
            find_id = index
            break
    return find_id


if __name__ == '__main__':
    a: list = [10, 3, 1, 4, 2]
    search_value: int = 4
    print(linear_search(a, search_value))
