# -*- coding = utf-8 -*-
# @Time : 2021/8/21 8:00
# @Author : 陈凡亮
# @File : Encode.py
# @Software : PyCharm

def main():
    # A 65
    # Z 90
    # a 97
    # z 122
    s=input()
    news=''

    for ss in s:
        if ss.isupper():
            if ord(ss)+4>90:
                news+=chr(ord(ss)+4-26)
            else:
                news+=chr(ord(ss)+4)
        else:
            if ord(ss)+4>122:
                news+=chr(ord(ss)+4-26)
            else:
                news+=chr(ord(ss)+4)
    print(news)


if __name__ == "__main__":
    main()
