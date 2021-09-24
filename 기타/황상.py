flag = 1
while flag == 1:
    snum = input("input: ")
    if (len(snum) % 2) != 0:
        flag = 1
        print("입력값의 길이가 짝수가 아닙니다.")

    else:
        flag = 0

mid = len(snum)//2
left_snum = snum[:mid]
right_snum = snum[mid:]

sum_left, sum_right = 0, 0

for i in range(0, mid):
    sum_left += int(left_snum[i])
    sum_right += int(right_snum[i])

print("left:", sum_left, "\nright:", sum_right)

if sum_left == sum_right:
    print("왼쪽 합 == 오른쪽 합")

else:
    print("왼쪽 합 != 오른쪽 합")
