# 最大値を求める

def max_list(array: list) -> int:
    for _index, num in enumerate(array):
        if _index != 0:
            comp_num = num if num >= comp_num else comp_num
        elif _index == 0:
            comp_num = num
    return comp_num


if __name__ == '__main__':
    a: list = [1, 3, 10, 2, 8]
    print(max_list(a))
