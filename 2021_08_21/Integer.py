# -*- coding = utf-8 -*-
# @Time : 2021/8/21 8:16
# @Author : 陈凡亮
# @File : Integer.py
# @Software : PyCharm

def main():
    n=input()
    print(len(n))
    s=''
    for nn in n:
        s+=nn+' '
    s.strip()
    print(s)
    news=s.split()

   # print(news)
    news.reverse()
   # print(news)
    re=''

    for ne in news:
        re+=ne
    print(re)


if __name__ == "__main__":
    main()
