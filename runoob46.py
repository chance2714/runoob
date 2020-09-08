#i = input('input a num, if quarter less than 50, exit: ')
again = 1
def sq(x):
    return x * x
while again:
    i = int(input('input a num'))
    print('result is %d' %(sq(i)))
    if sq(i) > 50:
        again = 1
    else:
        again = 0
        
