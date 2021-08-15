# 合計値を求める

def sum_list(array: list) -> int:
    sum_value: int = 0
    for num in array:
        sum_value += num
    return sum_value


if __name__ == '__main__':
    a: list = [1, 3, 10, 2, 8]
    print(sum_list(a))
