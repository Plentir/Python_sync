step = 0
def hanoi(n, frm, to):
    global step
    if n == 1:
        step += 1
        print("%4s, %s, %s ===> %s" %(step, n, frm, to))
    else:
        temp = 6 - frm - to
        hanoi(n-1, frm, temp)
        step += 1
        print("%4s, %s, %s => %s" %(step, n, frm, to))
        hanoi(n-1, temp, to)
hanoi(10, 1, 3)
# 20182827 윤주영
