# 합병 정렬
def Mrg(trg1, trg2):  #합병 모듈
	res = []
	i = j = 0
	while (i < len(trg1)) and (j < len(trg2)):
		if trg1[i] < trg2[j]:
			res.append(trg1[i])
			i += 1
		else:
			res.append(trg2[j])
			j += 1
	res += trg1[i:]
	res += trg2[j:]
	return res

def MrgSort(ary):
	if len(ary) <= 1:  #분할
		return ary

	mid = int(len(ary)/2)
	ary_l = MrgSort(ary[:mid])  #좌분할
	ary_r = MrgSort(ary[mid:])  #우분할
	return Mrg(ary_l, ary_r)

if __name__ == '__main__':
	print(MrgSort([47, 12, 32, 15, 55, 81, 97, 17]))