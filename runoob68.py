def move_step(step, l):
    if step > len(l):
        step_right = (step % len(l))
    else:
        step_right = step
    return step_right

def move_now(arrey, step):
    for i in range(step):
        arrey.insert(0, arrey.pop())
    return arrey

if __name__ == '__main__':
    step_right = 0
    l = list(input('please input some numbers: '))
    step = int(input('please input step you want to move: '))
    move_step(step, l)
    move_now(l, step_right)
    print(l)
