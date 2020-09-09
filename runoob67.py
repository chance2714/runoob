def inp():
    lo = input('please input a serveral numbers')
    li = list(lo)
    l = [int(x) for x in li]
def maxium(a,b):
    a,b = b,a
    return (a,b)
def minium(c,d):
    c,d = d,c
    return (c,d)
if __name__ == '__main__':
    inp()
    maxium(max(l),l[0])
    minium(min(l),l[-1])

