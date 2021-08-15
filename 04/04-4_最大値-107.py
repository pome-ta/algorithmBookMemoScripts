# 最大値を求める

def list_max(array: list) -> int:
    comp_num = 0
    for num in array:
        comp_num = num if num >= comp_num else comp_num
    return comp_num


if __name__ == '__main__':
    a: list = [1, 3, 10, 2, 8]
    print(list_max(a))
