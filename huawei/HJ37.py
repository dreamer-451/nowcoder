"""
HJ37 统计每个月兔子的总数

功能:
有一种兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子。
例子：假设一只兔子第3个月出生，那么它第5个月开始会每个月生一只兔子。
一月的时候有一只兔子，假如兔子都不死，问第n个月的兔子总数为多少？

数据范围：
输入满足 1 ≤ n ≤ 31

输入：
输入一个int型整数表示第n个月

输出：
输出对应的兔子总数
"""

'''
兔子：2月成长，后续开始成熟产子
第n月的兔子数为第n-1月的兔子数（成长期的兔子）和第n-2月的兔子数（成熟产子的兔子）
'''
def rabbits(m):
    if m == 1:
        return 1
    elif m == 2:
        return 1
    else:
        return rabbits(m - 1) + rabbits(m - 2)


if __name__ == '__main__':
    month = int(input())
    print(rabbits(month))
