class AutoProcessing:
    
    def __init__(self, line):
        self.__name = line.split()[0]
        self.__tel = line.split()[1]
        self.__id = line.split()[2]
        self.__mail = line.split()[-1]
        
        if self.__id.split("-")[-1][0] in ("9", "1", "3", "5", "7"):
            self.__sex = "Male"

        else:
            self.__sex = "Female"

    def seedata(self):
        print("Name:", self.__name)
        print("Tel.:", self.__tel)
        print("ID:", self.__id)
        print("E-mail:", self.__mail)
        print("Sex:", self.__sex)


def processor(index, splitter = None, target = None, start = 0, end = None):
    import os
    
    prc_data = []
        
    files = os.listdir(os.environ["USERPROFILE"] + "/desktop/과제2/")
    
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


def count(key = None):

    if key == "sex":  # 남자/여자 인원 수 세기
        n_male = n_female = 0
        
        data = processor(index = -2, splitter = "-", target = -1, end = 1)
        
        for i in data:
            if i in ("9", "1", "3", "5", "7"):
                n_male += 1
            
            else:
                n_female += 1
        
        print("Male:", n_male)
        print("Female:", n_female)
        
        return (n_male, n_female)
                    

    elif key == "portals":  # 가장 많이/적게 쓰는 포탈 찾기
        portals = processor(index = -1, splitter = "@", target = -1)

        user_num = {}

        for p in set(portals):
            user_num[p] = portals.count(p)

        temp = tuple(user_num.items())

        _mx = max(temp[n][-1] for n in range(len(temp)))
        _mn = min(temp[n][-1] for n in range(len(temp)))

        for n in range(len(temp)):
            
            if _mx is temp[n][-1]:
                most_used = temp[n][0]

            elif _mn is temp[n][-1]:
                least_used = temp[n][0]

        print("Most used portals: %s (%s)" %(most_used, _mx))
        print("Least used portals: %s (%s)" %(least_used, _mn))

        return user_num
                
        
    elif key == "ages":  # 가장 늙은/어린 사람의 나이 찾기
        raw_ages = processor(index = -2, splitter = "-", target = 0, end = 2)
        ages = []
        
        for n in range(len(raw_ages)):
            
            if int(raw_ages[n]) <= 19 and int(raw_ages[n]) >= 0:
                ages.append(19 - int(raw_ages[n]) + 1)
                
            else:
                ages.append(119 - int(raw_ages[n]) + 1)

        print("Youngest person: %s years old" %max(ages))
        print("Oldest person: %s years old" %min(ages))
        
        return (max(ages), min(ages))

    else:
        print("잘못된 인수를 입력했습니다.")
        
        return 1


if __name__ == "__main__":
    count("sex")
    count("portals")
    count("ages")
    