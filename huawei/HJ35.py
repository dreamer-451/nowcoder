"""
HJ35 蛇形矩阵

功能:
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

数据范围：
N不大于100

输入：
输入正整数N

输出：
输出一个N行的蛇形矩阵。

示例：
当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
"""

'''
第一行：1=(1*2)/2 3=(2*3)/2 6=(3*4)/2 10=(4*5)/2 15=(5*6)/2 
第二行：2=3-1 5=6-1 9=10-1 14=15-1
第三行：4=5-1 8=9-1 13=14-1
'''
if __name__ == '__main__':
    n = int(input())
    ans = [[]]
    for i in range(n):
        ans[0].append((i + 1) * (i + 2) // 2)
    for i in range(1, n):
        ans.append([num - 1 for num in ans[i - 1][1:]])
    for i in range(n):
        for j in range(n - i):
            print(ans[i][j], end=" ")
        print()
