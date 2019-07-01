def Calc(formular):
    if "^" in formular:
        idx = formular.index("^")
        formular.insert(idx - 1, float(formular[idx - 1]) ** float(formular[idx + 1]))

    elif "*" in formular:
        idx = formular.index("*")
        formular.insert(idx - 1, float(formular[idx - 1]) * float(formular[idx + 1]))

    elif "/" in formular:
        idx = formular.index("/")
        formular.insert(idx - 1, float(formular[idx - 1]) / float(formular[idx + 1]))

    elif "+" in formular:
        idx = formular.index("+")
        formular.insert(idx - 1, float(formular[idx - 1]) + float(formular[idx + 1]))

    elif "-" in formular:
        idx = formular.index("-")
        formular.insert(idx - 1, float(formular[idx - 1]) - float(formular[idx + 1]))

    del formular[idx : idx + 3]
    return formular


def operators(f, opr):
    index = f.index(opr)
    f.insert(index - 1, float(f[index - 1]))

    return f


def RunCalculator():
    fom = input("""계산할 수식을 입력하세요.
예) 1 + 3 * 3 ... (주의: 수와 연산 기호(+, -, *, ^, /)는 띄어쓰기로 구분합니다.)
입력: """).split()

    while len(fom) >= 3:
        Calc(fom)

    print("계산 결과: %s" %fom[0])
    return fom[0]


if __name__ == '__main__':
    RunCalculator()
