def inp():
    Numbers = input('please input a serveral numbers')
    List_str = list(Numbers)
    List_int = [int(x) for x in List_str]

def maxium(MaxNum,FirstNum):
    indexMax = List_int.index(MaxNum)
    List_int[indexMax],List_int[0] = FirstNum,MaxNum
    return (List_int)

def minium(MinNum,LastNum):
    indexMin = List_int.index(MinNum)
    List_int[indexMin],List_int[-1] = LastNum,MinNum
    return (List_int)

if __name__ == '__main__':
    Numbers = input('please input a serveral numbers: ')
    List_int = [int(x) for x in str(Numbers)]
    maxium(max(List_int),List_int[0])
    print(List_int)
    minium(min(List_int),List_int[-1])
    print(List_int)

