# 합병 정렬
def MrgSort(ary_input, low, high):
	mid = (low + high)/2
	if len(ary_input) >= 2 and low == 1:
		return MrgSort(ary_input, low, mid)
	elif len(ary_input) >= 2 and high == (len(ary_input) - 1):
		return MrgSort(ary_input, mid, high)
	
	else:
		ary = ary_input[low - 1 : 
		mid = (low + high)/2
	
	
	
if __name__ == '__main__':
	MrgSort([47, 12, 32, 15, 55, 81, 97, 17], 1, 8)

