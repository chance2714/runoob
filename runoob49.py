print('create lambda syntax')
maxmum = lambda x,y: (x>y)*x + (x<y)*y
minmum = lambda x,y: (x>y)*y + (x<y)*x
if __name__ == '__main__':
    a = int(input('input first number: '))
    b = int(input('input second number: '))
    print('the larger one is %d' % maxmum(a,b))
    print('the lower one is %d' % minmum(a,b))
