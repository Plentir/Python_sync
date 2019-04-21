# 합병 정렬
def Mrg(trg1, trg2):  #합병 및 정렬 모듈
	res = []
	i = j = 0
	while (i < len(trg1)) and (j < len(trg2)):  #오름차순 정렬
		if trg1[i] < trg2[j]:
			res.append(trg1[i])
			i += 1
		else:
			res.append(trg2[j])
			j += 1
	res += trg1[i:]  #비교가 필요없는 값(=이미 정렬된 값)을 뒤에 추가
	res += trg2[j:]  #위와 동일
	return res  #합병 및 정렬 결과 반환

def MrgSort(ary):  #분할 및 결과 출력 모듈
	if len(ary) <= 1:  #분할 중단 지점(재귀호출 종료점)
		return ary
	mid = int(len(ary)/2)
	ary_l = MrgSort(ary[:mid])  #좌분할
	ary_r = MrgSort(ary[mid:])  #우분할
	return Mrg(ary_l, ary_r)  #좌분할&우분할 병합

if __name__ == '__main__':
	print(MrgSort([47, 12, 32, 15, 55, 81, 97, 17]))