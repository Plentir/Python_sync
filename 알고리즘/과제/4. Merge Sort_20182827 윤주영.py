# 합병 정렬
def MrgSort(ary):
	mid = len(ary)/2
	if len(ary) > 1:  #분할
		MrgSort(ary[:mid])  #좌분할
		MrgSort(ary[mid:])  #우분할
		#Mrg(a, b)

def Mrg(trg1, trg2):  #합병 모듈
	res = []
	idx_trg1 = 0
	idx_trg2 = 0
	while (idx_trg1 <= len(trg1) - 1) and (idx_trg2 <= len(trg2) - 1):
		if trg1[idx_trg1] < trg2[idx_trg2]:
			res.append(trg1[idx_trg1])
			idx_trg1 += 1
		else:
			res.append(trg2[idx_trg2])
			idx_trg2 += 1
	if (idx_trg1 > len(trg1) - 1) and (idx_trg2 < len(trg2) - 1):  #trg1은 전부 추가됨 & trg2는 남은 게 있음.
		for i in range(idx_trg2, len(trg2)):
			res.append(trg2[i])
	elif (idx_trg1 < len(trg1) - 1) and (idx_trg2 > len(trg2) - 1):  #trg1은 남은 게 있음 & trg2는 전부 추가됨.
		for i in range(idx_trg1, len(trg1)):
			res.append(trg1[i])
	return res

"""
def Compare(ary1, idx_ary1, ary2, idx_ary2):
	res = []
	pos = 0
	if ary1[idx_ary1] < ary2[idx_ary2]:
		res.append(ary1[idx_ary1])
		idx_ary1 += 1
		pos += 1
	else:
		res.append(ary2[idx_ary2])
		idx_ary2 += 1
		pos += 1
	return (res, pos)

Compare(trg1, idx_trg1, trg2, idx_trg2)
"""
if __name__ == '__main__':
	#MrgSort([47, 12, 32, 15, 55, 81, 97, 17])
	print(Mrg([47, 12, 32, 15], [55, 81, 97, 17]))

