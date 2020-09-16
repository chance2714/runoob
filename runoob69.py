if __name__ == '__main__':
    nmax = int(input('please input people count: '))
    nlist = []
    set_count = nmax // 3
    set_out = nmax % 3
    for _ in range(set_count):
        for i in range(1,4):
            nlist.append(i)
    if set_out == 2:
        nlist.append(1)
        nlist.append(2)
    elif set_out == 1:
        nlist.append(1)
    print(nlist)
    while len(nlist) > 2:
        three_plus = lambda x: x
        ll = list(filter())
