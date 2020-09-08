def exchange(a,b):
    a,b = b,a
    return (a,b)
if __name__ == '__main__':
    a = input('input num 1')
    b = input('input num 2')
    print('a = {},b = {}'.format(a,b))
    a,b = exchange(a,b)
    print('a = {},b = {}'.format(a,b))
