res = []

def MrgSort(ary_input, low, high): # low ~ high까지의 범위를 가진 리스트.
    global res
    mid = int((low + high)/2)
    if low < high: # 분할한 두 리스트의 길이가 각각 1이 될 때까지 분할.
        #ary_ld = ary_input[low - 1 : mid] 
        MrgSort(ary_input, low, mid) # 앞쪽 리스트(idx = 0 ~ 절반)
        #ary_flw = ary_input[mid : high - 1] 
        MrgSort(ary_input, mid + 1, high) # 뒤쪽 리스트(idx = 절반 ~ 끝)
        Mrg(ary_input, low, high, mid)
    return res

def Mrg(ary_input, low, high, mid): # 요소들을 오름차순 정렬하고 병합.
    global res
    i = low - 1
    j = mid - 1
    while i <= mid and j <= high:
        if ary_input[i] < ary_input[j]:
            res.append(ary_input[i])
            i += 1
        else:
            res.append(ary_input[j])
            j += 1

if __name__ == '__main__':
    MrgSort([45, 7, 2, 36, 61, 25, 22, 15], 1, 8)