# バイナリサーチ(二分探索法)で探索する


def binary_search(array: list, search: int) -> int:
    find_id: int = -1
    left: int = 0
    right: len(array) -1
    for index, num in enumerate(array):
        if search == num:
            find_id = index
            break
    return find_id


if __name__ == '__main__':
    a: list = [1,2,4,5,10]
    search_value: int = 4
    print(binary_search(a, search_value))

