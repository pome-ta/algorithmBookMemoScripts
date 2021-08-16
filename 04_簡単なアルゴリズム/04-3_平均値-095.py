# 平均値を求める


def average_list(_array: list) -> float:
    len_array: int = len(_array)
    sum_value: int = 0
    for num in _array:
        sum_value += num
    return sum_value / len_array


if __name__ == '__main__':
    a: list = [1, 3, 10, 2, 8]
    print(average_list(a))
