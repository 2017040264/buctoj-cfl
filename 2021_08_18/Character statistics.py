# -*- coding = utf-8 -*-
# @Time : 2021/8/18 9:05
# @Author : 陈凡亮
# @File : Character statistics.py
# @Software : PyCharm

def main():
    letter_count=0
    digit_count=0
    blank_count=0
    other_count=0
    s=input()
    for ss in s:
        if str(ss).isalpha():
            letter_count+=1
        elif str(ss).isdigit():
            digit_count+=1
        elif str(ss)==' ':
            blank_count+=1
        else:
            other_count+=1
    print(letter_count,digit_count,blank_count,other_count)



if __name__ == "__main__":
    main()
