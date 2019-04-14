fom = input("""계산할 수식을 입력하세요.
예) 1 + 3 * 3 ... (주의: 수와 연산 기호(+, -, *, ^, /)는 띄어쓰기로 구분합니다.)
입력: """).split()

while len(fom) >= 3:
    if "^" in fom:
        idx = fom.index("^")
        fom.insert(idx - 1, float(fom[idx - 1]) ** float(fom[idx + 1]))
        del fom[idx : idx + 3]

    elif "*" in fom:
        idx = fom.index("*")
        fom.insert(idx - 1, float(fom[idx - 1]) * float(fom[idx + 1]))
        del fom[idx : idx + 3]

    elif "/" in fom:
        idx = fom.index("/")
        fom.insert(idx - 1, float(fom[idx - 1]) / float(fom[idx + 1]))
        del fom[idx : idx + 3]

    elif "+" in fom:
        idx = fom.index("+")
        fom.insert(idx - 1, float(fom[idx - 1]) + float(fom[idx + 1]))
        del fom[idx : idx + 3]

    elif "-" in fom:
        idx = fom.index("-")
        fom.insert(idx - 1, float(fom[idx - 1]) - float(fom[idx + 1]))
        del fom[idx : idx + 3]

print("계산 결과: %s" %fom[0])
