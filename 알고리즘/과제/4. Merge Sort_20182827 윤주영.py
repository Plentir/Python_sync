# 합병 정렬
def Mrg(trg1, trg2):  #합병 모듈
	res = []
	a = len(trg1)
	b = len(trg2)
	i = j = 0
	while (i < a) and (j < b):
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
		print(ary)
		return ary

	mid = int(len(ary)/2)
	ary_l = MrgSort(ary[:mid])  #좌분할
	ary_r = MrgSort(ary[mid:])  #우분할
	print(ary_l, ary_r)
	return Mrg(ary_l, ary_r)

if __name__ == '__main__':
	print(MrgSort([47, 12, 32, 15, 55, 81, 97, 17]))