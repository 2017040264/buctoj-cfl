n = int(input())
for i in range(n):
    m = int(input())

    st = input().split()
    st = st[:m]

    for j in range(m):
        st[j] = int(st[j])

    seta = list(set(st))

    seta.sort()

    if len(seta) < 2:
        print("NO")
    else:
        print(seta[1])