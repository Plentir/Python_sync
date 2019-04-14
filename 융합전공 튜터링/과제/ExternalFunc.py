"""
1. C 드라이브 밑에 자신의 이름으로 만든 디렉토리를 생성
2. 해당 디렉토리 안에 내가 준 파일을 옮기고(바탕화면에 저장한 후 (복사X)옮기세요)
3. 압축을 푼 후
4. 파일을 분류
txt - 1,2,3,4,5,6,7...
py - 1p,2p,3p 확장자를 .txt로 바꾸세요
bat - 현재 시간(밀리초까지)
jpg - a,b,c,d...
"""
import os
import time

def MkMvRn(folder, file):
    os.mkdir("c:\\%s" %folder) # 디렉터리 생성. - 1번
    os.system("move %s c:\\%s\\%s" %(file, folder, file.split("\\")[-1])) # 생성한 디렉터리로 파일 이동. - 2번
    os.startfile("c:\\%s\\%s" %(folder, file.split("\\")[-1])) # 이동한 파일을 실행. - 3번
    return 1

def AutoCat(path):
    files = os.listdir(path)
    file_list = []
    for file in files: # 파일 목록 생성
        file_list.append(file)

    os.chdir(path)
    for i in range(len(file_list)):
        if file_list[i].split(".")[-1] == "txt":
            for i in range(len(file_list)): # .txt 파일 이름 변경(완성)
                os.rename(file_list[i], "%s.txt" %i)
        
        elif "p" in file_list[i].split(".")[-1][-1]:
            for i in range(len(file_list)): # .py 파일 이름 변경(완성)
                os.rename(file_list[i], "%s.txt" %(file_list[i].split(".")[0]))

        elif file_list[i].split(".")[-1] == "bat":
            for i in range(len(file_list)): # .bat 파일 이름 변경(미완)
                os.rename(file_list[i], "%s.bat" %(time.time_ns()))

        elif file_list[i].split(".")[-1] == "jpg":
            for i in range(len(file_list)): # .jpg 파일 이름 변경(완성)
                os.rename(file_list[i], "%s.jpg" %chr(i + 65).lower())
        
    return 1
    
if __name__ == "__main__":
    #MkMvRn("윤주영", "c:\\users\\yjy99\\desktop\\과제.zip")
    AutoCat("C:\\윤주영\\과제\\과제")