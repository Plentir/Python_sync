import time

def Fibonacci(n): #재귀적 프로그래밍
    if n >= 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

    elif n == 1:
        return 1
        
    else:
        return 0

t_s = time.time_ns() #타이머 시작
print(Fibonacci(30)) #프로그램 실행
t_Fibonacci_e = time.time_ns() #타이머 종료
print("Running time: %.8fsec." % ((t_Fibonacci_e - t_s)/1000000000)) #실행 시간 출력

def Fibo(n): #동적 프로그래밍
    seq_fibo = [0, 1]
    if n >= 2:
        for i in range(0, n - 1):
            seq_fibo.append(seq_fibo[i + 1] + seq_fibo[i])
        return seq_fibo[-1]

    elif n == 1:
        return 1

    else:
        return 0

t_s = time.time_ns() #타이머 시작
print(Fibo(30)) #프로그램 실행
t_fibo_e = time.time_ns() #타이머 종료
print("Running time: %.8fsec." % ((t_fibo_e - t_s)/1000000000)) #실행 시간 출력
