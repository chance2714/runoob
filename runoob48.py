while 1:
    a = input('input a')
    b = input('input b')
    def bigger(a,b):
        print('{} > {}'.format(a,b))
    def less(a,b):
        print('{} < {}'.format(a,b))
    def equal(a,b):
        print('{} = {}'.format(a,b))
    if a>b:
        bigger(a,b)
    elif a<b:
        less(a,b)
    elif a==b:
        equal(a,b)
    else:
        print('unknown')
