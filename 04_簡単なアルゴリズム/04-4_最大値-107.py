# 最大値を求める


def max_list(_array: list) -> int:
    comp_num: int = -1
    for index, num in enumerate(_array):
        if index != 0:
            comp_num = num if num >= comp_num else comp_num
        elif index == 0:
            comp_num = num
    return comp_num


if __name__ == '__main__':
    a: list = [1, 3, 10, 2, 8]
    print(f'最大値: {max_list(a)}')
