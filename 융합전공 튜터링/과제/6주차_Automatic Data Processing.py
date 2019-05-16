class AutoProcessing:
    
    def __init__(self, line):
        self.__temp = line.split()

        self.__name = self.__temp[0]
        self.__tel = self.__temp[1]
        self.__id = self.__temp[2]
        self.__mail = self.__temp[-1]


    def seedata(self):
        print("Raw data:", self.__temp)
        print("Name:", self.__name)
        print("Tel.:", self.__tel)
        print("ID:", self.__id)
        print("E-mail:", self.__mail)


    def sex(self):
        if self.__id.split("-")[-1][0] in ["9", "1", "3", "5", "7"]:
            self.__sex = "Male"

        else:
            self.__sex = "Female"

        print("Sex:", self.__sex)


def count(dir, key = "sex"):
		
	if key == "sex":
		n_male = n_female = 0
		
		data = processor(index = -2, splitter = "-", target = -1, end = 0)
		
		result = []
		
		for i in data:
			if i in ("9", "1", "3", "5", "7"):
				pcr_data.append("Male")
			
			
			else:
				prc_data.append("Female")
		
		return result
				
		"""
		for i in files:
			f = open(os.environ["USERPROFILE"] + "/desktop/과제2/" + i, "r")
			
			raw_data = f.readline().split()
			
			if raw_data[2].split("-")[0] in [1, 3, 5, 7, 9]:
				n_male += 1
			
			else:
				n_female += 1
				
			f.close()
		"""		
	
	elif key == "portals":
		portals = processor(index = -1, splitter = "@", target = -1)
		
		_min = _max = 0
		user_num = {}
		
		for p in set(portals):
			print(portals.count(p))
			
			if 
			user_num[p] = portals.count(p)
		
		temp = user_num.items()
		
			
			
		return user_num
				
	elif key == "ages":
		ages = processor(index = -2, splitter = "-", target = 0, end = 1)
	
	
	else:
		print("잘못된 인수를 입력했습니다.")
		

def processor(index, splitter = "", target = None, start = 0, end = -1):
	import os
	
	prc_data = []
		
	files = os.listdir(dir)
	
	if target is None:
		for i in files:
			f = open(os.environ["USERPROFILE"] + "/desktop/과제2/" + i, "r")
			
			raw_data = f.readline().split()
			
			prc_data.append(raw_data[index].split(splitter)[start : end])
			
			f.close()
	
	else:
		for i in files:
			f = open(os.environ["USERPROFILE"] + "/desktop/과제2/" + i, "r")
			
			raw_data = f.readline().split()
			
			prc_data.append(raw_data[index].split(splitter)[target][start : end])
			
			f.close()
	
	return prc_data


if __name__ == "__main__":
    test = AutoProcessing("윤승민	010-2039-3139	121203-1497872	AY4312@hanmail.net")

    test.seedata()

    test.sex()
