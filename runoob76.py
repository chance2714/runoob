def even(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += 1.0/i
    return sum

def odd(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += 1.0/i
    return sum

if __name__ == '__main__':
    n = int(input('input a number: '))
    if n % 2 == 0:
        nsum = even(n)
    elif (n+1) % 2 == 0:
        nsum = odd(n)
    print(nsum)
