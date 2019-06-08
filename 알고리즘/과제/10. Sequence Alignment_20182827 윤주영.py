def print_array(ary, seq_ref, seq_target):
    """It prints a 2-dimensional array to (col * row) size grid form."""

    col = len(seq_ref)
    row = len(seq_target)

    print(" " * 3, end = "")  # 가로축 정렬 맞춰줌.
    for i in range(col):  # 가로축 출력.
        print(("%2s " %seq_ref[i]) if (i != col - 1) else ("%2s\n" %seq_ref[i]), end = "")
    
    for i in range(row):
        print("%2s " %seq_target[i], end = "")  # 세로축 출력.

        for j in range(col):
            print(("%2s " %ary[i][j]) if (j != col - 1) else ("%2s\n" %ary[i][j]), end = "")  # 값 출력.

    return


def update_value(row, col, array):
    """Re-calculate the value of the cell."""
    # The parameter 'row' and 'col' can not be larger than -1.

    value = array[row][col]

    col_max = max(array[ro][col + 1] for ro in range(row + 1, 0))  # 가로 방향 최댓값 검색.
    row_max = max(array[row + 1][co] for co in range(col + 1, 0))  # 세로 방향 최댓값 검색.

    value += max(col_max, row_max)  # 최종적으로 더할 값 결정.

    return value


def summatrix(seq_ref, seq_target):
    """It calculates a alignment score and makes a decision how to align the seqs."""

    row = len(seq_target)
    col = len(seq_ref)

    array = [[1 if seq_ref[co] is seq_target[ro] else 0 for co in range(col)] for ro in range(row)]  # 참조 서열 길이 x 대조 서열 길이 크기의 2차원 배열 생성. 
    print("<Initialize>")
    print_array(array, seq_ref, seq_target)

    # 값을 업데이트함.
    for ro in range(-1, -(row + 1), -1):  # row(참조 서열 길이)만큼 반복.

        for co in range(-1, -(col + 1), -1):  # col(대조 서열 길이)만큼 반복.
            if (ro != -1) and (co != -1):
                array[ro][co] = update_value(ro, co, array)

    print("\n<Result>")
    print_array(array, seq_ref, seq_target)
    print("\n#END")

    return array


def modarray(array):
    """It modifies an array to fittable form for a sequence alignment."""
    
    (row, col) = (len(array), len(array[0]))

    for ro in range(row):  # 열 방향으로 배열 길이 2만큼 연장.
        array[ro].append(-1)
        array[ro].append(-1)
    
    for i in range(2):
        array.append([-1 for co in range(col + 2)])  # 행 방향으로 배열 길이 2만큼 연장.
    
    return array


def alignseq(array, seq_ref, seq_target):
    """Align the sequence by using the sum matrix."""

    (row_max, col_max, row, col) = (len(seq_target), len(seq_ref), 0, 0)  # 초기화.
    align_ref = align_target = ""
    
    ary_mod = modarray(array)  # Index error
    
    while (row < row_max) and (col < col_max):  # 모두 정렬할 때까지 반복.
        next_max = max(ary_mod[row + 1][col + 1], ary_mod[row + 1][col + 2], ary_mod[row + 2][col + 1])

        if ary_mod[row + 1][col + 1] == next_max:  # 대각선 방향으로 이동.
            align_ref += seq_ref[col]
            align_target += seq_target[row]
            
            col += 1
            row += 1
        
        elif ary_mod[row + 1][col + 2] == next_max:  # 오른쪽으로 이동.
            align_ref += seq_ref[col:col + 2]
            align_target += seq_target[row] + "-"
            
            col += 2
            row += 1

        elif ary_mod[row + 2][col + 1] == next_max:  # 아래쪽으로 이동.
            align_ref += seq_ref[col] + "-"
            align_target += seq_target[row:row + 2]
            
            col += 1
            row += 2
    
    align_ref += seq_ref[col:]  # 남은 문자열 붙임.
    align_target += seq_target[row:]  # 남은 문자열 붙임.
    
    print("[Reference seq.]\n>>", align_ref, "\n>>", align_target, "\n[Target seq.]")

    return (align_ref, align_target)


if __name__ == "__main__":
    seq_ref = "ABCNYRQCLCRPM"  # col
    seq_target = "AYCYNRCKCRBP"  # row

    ary = summatrix(seq_ref, seq_target)

    print("\n############START ALIGNMENT############\n")

    alignseq(ary, seq_ref, seq_target)