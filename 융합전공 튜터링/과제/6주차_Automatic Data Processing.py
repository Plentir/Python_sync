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


def count(self, dir, key = "sex"):
	import os
	
	files = os.listdir(dir)
	
	if key == "sex":
		self.n_male = self.n_female = 0

		for i in files:
			f = open(os.environ["USERPROFILE"] + "/desktop/과제2/" + i, "r")
			
			raw_data = f.readline().split()
			
			if raw_data[2].split("-")[0] in [1, 3, 5, 7, 9]:
				n_male += 1
			
			else:
				n_female += 1
				
			f.close()
				
	
	elif key == "portals":
		portals = []
		
		for i in files:
			f = open(os.environ["USERPROFILE"] + "/desktop/과제2/" + i, "r")
			
			raw_data = f.readline().split()
			
			portals.append(raw_data[-1].split("@")[-1])
			
		for p in set(portals):
			print(portals.count(p))
			
	
	else:
		print("올바르지 않은 인수.")



if __name__ == "__main__":
    test = AutoProcessing("윤승민	010-2039-3139	121203-1497872	AY4312@hanmail.net")

    test.seedata()

    test.sex()
