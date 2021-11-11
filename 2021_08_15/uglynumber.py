# -*- coding = utf-8 -*-
# @Time : 2021/7/1 8:34
# @Author : 陈凡亮
# @File : uglynumber.py
# @Software : PyCharm

def main():
    n=1352
    nthUglyNumber(n)

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """

    result = [1]
    i = 2
    while (len(result) <= n):
        m = i
        while (m % 2 == 0):
            m = m / 2
        while (m % 3 == 0):
            m = m / 3
        while (m % 5 == 0):
            m = m / 5

        if m == 1:
            result.append(i)
        i = i + 1

    print(result)
    print(n)
    print(result[n-1])
    return result[n - 1]

def nthUglyNumber1(n):
    """
    :type n: int
    :rtype: int
    """

    result = [1]
    a2 = 0
    a3 = 0
    a5 = 0
    while (len(result) <= n):
        small = min(result[a2] * 2, min(result[a3] * 3, result[a5] * 5))
        result.append(small)
        if result[a2] * 2 == small:
            a2 += 1
        if result[a3] * 3 == small:
            a3 += 1
        if result[a5] * 5 == small:
            a5 += 1

    return result[n - 1]


if __name__ == "__main__":
    main()
