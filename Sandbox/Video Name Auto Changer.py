import os

class AutoChanger():

    def __init__(self, dir):
        self.__dir = dir

        self.__file_names = os.listdir(self.__dir)
        self.__file_formats = [f[-3:] for f in self.__file_names]
        
        return


    def getRules(self):
        if self.__sep == " ":
            print("Naming rules updated!\n >Directory: %s\n >Title: %s\n >Year: %s\n >Separator: %s" \
                %(self.__dir, self.__title, self.__year, "Blank"))

        elif self.__sep == "\t":
            print("Naming rules updated!\n >Directory: %s\n >Title: %s\n >Year: %s\n >Separator: %s" \
                %(self.__dir, self.__title, self.__year, "Tab"))

        else:
            print("Naming rules updated!\n >Directory: %s\n >Title: %s\n >Year: %s\n >Separator: %s" \
                %(self.__dir, self.__title, self.__year, self.__sep))

        return


    def setRules(self, title="none", year="none", sep=" "):
        if title == "none":
            self.__title = self.__dir.split("\\")[-1]

        else:
            self.__title = title

        self.__year = year
        self.__sep = sep

        self.getRules()

        return


    def getFiles(self):
        file_no = 1

        for l in self.__file_names:
            print("File_%s: %s" %(file_no, l))
            file_no += 1
    
        return


    def getFlieForms(self):
        file_no = 1

        for l in self.__file_formats:
            print("File_%s: %s" %(file_no, l))
            file_no += 1
        
        return
        
    
    def changeName(self):
        self.getRules()
        flag = input("계속 진행할까요? [y, n]\n입력: ")

        if flag in ("n", "N", "no", "No", "NO"):
            print("취소됨.")
            return

        elif flag in ("y", "Y", "yes", "Yes", "YES"):
            os.chdir(self.__dir)
            file_no = 0

            for name in self.__file_names:
                os.rename(name, "%s - %02d.%s" %(self.__title, (file_no + 1), self.__file_formats[file_no]))
                file_no += 1

        print("완료됨.")

        return
            

if __name__ == "__main__":
    test = AutoChanger("D:\\Media\\영상\\Movies\\애니메이션\\카게구루이 XX")
    
    test.setRules(title="Kagegurui XX")
    test.getFiles()
    test.changeName()
