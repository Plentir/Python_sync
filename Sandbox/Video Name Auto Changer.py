import os

class AutoChanger():

    def __init__(self, dir):
        self.__dir = dir

        self.__file_names = os.listdir(self.__dir)
        self.__file_formats = [f[-3:] for f in self.__file_names]


    def setRules(self, title="none", year="none", sep=" "):
        if title == "none":
            self.__title = self.__dir.split("\\")[-1]

        else:
            self.__title = title

        self.__year = year
        self.__sep = sep

        if self.__sep == " ":
            print("Naming rules updated!\n >Directory: %s\n >Title: %s\n >Year: %s\n >Separator: %s" \
                %(self.__dir, self.__title, self.__year, "Blank"))

        elif self.__sep == "\t":
            print("Naming rules updated!\n >Directory: %s\n >Title: %s\n >Year: %s\n >Separator: %s" \
                %(self.__dir, self.__title, self.__year, "Tab"))

        else:
            print("Naming rules updated!\n >Directory: %s\n >Title: %s\n >Year: %s\n >Separator: %s" \
                %(self.__dir, self.__title, self.__year, self.__sep))


    def getFiles(self):
        file_no = 1

        for l in self.__file_names:
            print("File_%s: %s" %(file_no, l))
            file_no += 1
    

    def getFlieForms(self):
        file_no = 1

        for l in self.__file_formats:
            print("File_%s: %s" %(file_no, l))
            file_no += 1

if __name__ == "__main__":
    test = AutoChanger("D:\\Media\\영상\\Movies\\애니메이션\\Pop Team Epic")
    
    test.setRules()
    test.getFiles()