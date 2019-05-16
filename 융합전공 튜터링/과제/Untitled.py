"""
1. 남자와 여자를 주민번호를 통해 몇 명 있는지 분류하라
2. 가장 많이 쓰는 웹사이트(이메일을 보고 판단)은 무엇인가
3. 가장 나이가 많은 사람과 가장 나이가 어린 사람은 몇 살인가
4. 잘못된 주민번호가 있다면 찾고 이유를 밝혀라
"""

def count(dir, key = "sex"):
		
	if key == "sex":
		n_male = n_female = 0
		
		for i in files:
			f = open(os.environ["USERPROFILE"] + "/desktop/과제2/" + i, "r")
			
			raw_data = f.readline().split()
			
			if raw_data[2].split("-")[0] in [1, 3, 5, 7, 9]:
				n_male += 1
			
			else:
				n_female += 1
				
			f.close()
				
	
	elif key == "portals":
		portals = processor(-1, "@", start = -1)
			
		for p in set(portals):
			print(portals.count(p))
			
	elif key == "ages":
		ages = processor(-2, "-", )
		
		
	
	else:
		print("잘못된 인수를 입력했습니다.")
		

def processor(index, spliter, start = 0, end = -1 target):
	import os
	
	prc_data = []
		
	files = os.listdir(dir)
	
	if int target is exist:
		for i in files:
			f = open(os.environ["USERPROFILE"] + "/desktop/과제2/" + i, "r")
			
			raw_data = f.readline().split()
			
			prc_data.append(raw_data[index].split(spliter)[target][start : end])
			
			f.close()
	
	else:
		for i in files:
			f = open(os.environ["USERPROFILE"] + "/desktop/과제2/" + i, "r")
			
			raw_data = f.readline().split()
			
			prc_data.append(raw_data[index].split(spliter)[start : end])
			
			f.close()
	
	return prc_data
