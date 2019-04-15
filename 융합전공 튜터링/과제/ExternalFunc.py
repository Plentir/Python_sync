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
    try:
        os.mkdir("c:\\%s" %folder) # 디렉터리 생성. - 1번
        os.system("move %s c:\\%s\\%s" %(file, folder, file.split("\\")[-1])) # 생성한 디렉터리로 파일 이동. - 2번
        os.startfile("c:\\%s\\%s" %(folder, file.split("\\")[-1])) # 이동한 파일을 실행. - 3번
        for i in range(1, 6):
            print("Work in Progress... %s seconds remain." %(6 - i))
            time.sleep(1) # 압축 해제 완료 시까지 대기 = 5초

    except FileExistsError:
        print("Can not make directory. The folder or file already exists.")
    return 1

def AutoCat(path):
    files = os.listdir(path)
    file_list = []
    for f in files: # 파일 목록 생성(변경할 파일 목록 작성)
        file_list.append(f)

    os.chdir(path)
    cnt_txt = 0
    cnt_py = 0
    cnt_jpg = 0
    for i in file_list: # 변경 과정 반복
        if i.split(".")[-1] == "txt": # .txt 파일 이름 변경(완성)
            cnt_txt += 1
            os.rename(i, "%s.txt" %cnt_txt)
        
        elif i.split(".")[-1] == "py": # .py 파일 이름 변경(완성)
            cnt_py += 1
            os.rename(i, "%sp.txt" %cnt_py)

        elif i.split(".")[-1] == "bat": # .bat 파일 이름 변경(미완)
            now = time.strftime("%Y%m%d_%Hh_%Mm_%S", time.localtime(time.time()))
            now += str(time.time())[10:14] # 소수점 아래 3자리(ms)만 추출하려 했는데 파일 이름 충돌 일어남.
            os.rename(i, "%ss.bat" %now)
            time.sleep(0.001)

        elif i.split(".")[-1] == "jpg": # .jpg 파일 이름 변경(완성)
            cnt_jpg += 1
            os.rename(i, "%s.jpg" %chr(cnt_jpg + 64).lower())
    return 1

if __name__ == "__main__":
    MkMvRn("윤주영", "c:\\users\\yjy99\\desktop\\과제.zip")
    #AutoCat("C:\\윤주영\\과제\\과제") # 압축파일 이름으로 폴더 만들어서 압축 해제 옵션을 사용할 경우에 사용.
    AutoCat("C:\\윤주영\\과제")