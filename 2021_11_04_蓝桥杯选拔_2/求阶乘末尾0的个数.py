
while True:
    try:
        n=int(input())
        re=0
        while n>=5:

            n=n//5
            re+=n

        print(re)

    except:
        break

