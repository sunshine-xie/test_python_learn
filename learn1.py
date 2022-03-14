# 循环嵌套

def multiple_table():
    """

    打印乘法表

    """

    row = 1
    while row <= 9:
        col = 1  # 列每次都是从1开始
        while col <= row:
            print("%d * %d = %d" % (col, row, col * row), end="\t")
            col += 1
        print("")
        row += 1


def sum_2_sum(num1, num2):
    """
    两个数加法运算
    :param num1: 被加数
    :param num2: 加数
    :return: 和
    """
    result = num1 + num2
    print("%.3f + %.3f = %.3f" % (num1, num2, result))
    return result



