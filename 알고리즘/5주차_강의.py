"""
def hanoi(n, frm, to):
    if n == 1:
        print(frm, "->", to)
    else:
        temp = 6 - frm - to
        hanoi(n-1, frm, temp)
        print(frm, "->", to)
        hanoi(n-1, temp, to)
"""
"""
ary = [1, 124, 22, 12452, 52, 612, 5, 7, 111123, 123]
minn = ary[0]
maxx = ary[0]

for i in range(len(ary)):
    if ary[i] < minn:
        minn = ary[i]

for j in range(len(ary)):
    if ary[j] > maxx:
        maxx = ary[j]

print(minn, maxx)
"""
item_list = [[60, 4], [45, 9], [21, 7], [12, 3]] #["total price", "weight"]
ppw = [] #price per weight

for i in range(len(item_list)):
    ppw.append((item_list[i][0]/item_list[i][1]))

limit_w = 15 #weight limitation
