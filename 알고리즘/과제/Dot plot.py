
def print_array(ary):
    """It prints a 2-dimensional array to ("row" * "col.") size grid form."""

    row = len(ary[0])  # 가로 길이
    col = len(ary)  # 세로 길이

    for i in range(col):

        for j in range(row):
            print(("%2s " %ary[i][j]) if (j != row - 1) else ("%2s\n" %ary[i][j]), end = "")
    
    return


def update_value(row, col, array):
    """Re-calculate and update the value of a cell."""

    


    return array


def dotplot(sequence_ref, sequence_target):
    """It calculates a alignment score and make a decision how to align the sequences."""

    row = len(sequence_ref)
    col = len(sequence_target)

    array = [[0 for i in range(row)] for j in range(col)]  # 참조 서열 길이 x 대조 서열 길이 크기의 2차원 배열 생성.
    print_array(array)


    for co in range(col):  # col(대조 서열 길이)만큼 반복

        for ro in range(row):  # row(참조 서열 길이)만큼 반복
            array[co][ro]



if __name__ == "__main__":
    seq_ref = "ABCNYRQCLCRPM"
    seq_target = "AYCYNRCKCRBP"
    dotplot(seq_ref, seq_target)
    