def F(n):

    f_list = []

    n1 = 0
    n2 = 1

    for i in range(0,n):
        nn = n1
        n1 = n2
        n2 = nn+n1
        f_list.append(nn)

    return f_list

print(F(10))