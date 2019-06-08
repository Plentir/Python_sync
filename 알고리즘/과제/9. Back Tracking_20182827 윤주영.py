B = [1, 2, 3, 4, 5, 6, 7, 8]
n = 8

cnt_sol = 0
cnt_exp = 0

def place(k):
    global B, n, cnt_exp
    
    i = 0
    cnt_exp += 1
    while i < k:
        if (B[i] == B[k]) or (abs(B[i] - B[k]) == abs(i - k)):
            return False
        
        i += 1
        
    return True


def queens(k):
    global B, n, cnt_sol, cnt_exp
    
    for i in range(n):
        B[k - 1] = i + 1
        
        if place(k - 1) == True:
            if k == n:
                cnt_sol += 1
                print(cnt_exp, cnt_sol, B, sep = " // ")

            else:
                queens(k + 1)


if __name__ == "__main__":
    queens(1)
