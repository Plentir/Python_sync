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

def MkMvRn(folder, file):  # 디렉터리 생성 ~ 압축 해제
    try:
        os.mkdir("c:\\%s" %folder)  # 디렉터리 생성. - 1번
        os.system("move %s c:\\%s\\%s" %(file, folder, file.split("\\")[-1])) # 생성한 디렉터리로 파일 이동. - 2번
        fo_dst = file.split("\\")[-1]
        os.startfile("c:\\%s\\%s" %(folder, fo_dst))  # 이동한 파일을 실행. - 3번
        for i in range(1, 6):
            print("Work in progress... %s seconds remain." %(6 - i))
            time.sleep(1)  # 압축 해제 완료 시까지 대기 = 5초

    except FileExistsError:  # 파일 또는 폴더가 이미 존재할 때
        print("Can not make directory. The folder or file already exists.")
    except FileNotFoundError:  # 파일 또는 폴더가 존재하지 않을 때
        print("The file is not found. Can not go on the processes.")

    return AutoCat("c:\\%s\\%s" %(folder, fo_dst.split(".")[0]))
"""
def ReName(origin, dst_file, cnter):
    os.rename(origin, "%s.%s" %(cnter,))
"""
def AutoCat(path):  # 파일 분류 및 이름 재설정
    try:
        files = os.listdir(path)
        file_list = []
        for f in files:  # 파일 목록 생성(변경할 파일 목록 작성)
            file_list.append(f)

        os.chdir(path)  # 압축을 해제한 폴더 내에서 작업 진행.
        cnt_txt = 0
        cnt_py = 0
        cnt_jpg = 0
        for i in file_list:  # 변경 과정 반복
            if i.split(".")[-1] == "txt":  # .txt 파일 이름 변경
                cnt_txt += 1
                os.rename(i, "%s.txt" %cnt_txt)
            
            elif i.split(".")[-1] == "py":  # .py 파일 이름 변경
                cnt_py += 1
                os.rename(i, "%sp.txt" %cnt_py)

            elif i.split(".")[-1] == "bat":  # .bat 파일 이름 변경
                now = time.strftime("%Y%m%d_%Hh_%Mm_%S", time.localtime(time.time()))
                now += str(time.time())[10:14]
                os.rename(i, "%ss.bat" %now)
                time.sleep(0.001)  # 파일 이름 충돌 방지
                
            elif i.split(".")[-1] == "jpg":  # .jpg 파일 이름 변경
                cnt_jpg += 1
                os.rename(i, "%s.jpg" %chr(cnt_jpg + 64).lower())
        print("File re-naming have been successfully done.")
        
    except FileExistsError:  # 파일 또는 폴더가 이미 존재할 때
        print("Can not make directory. The folder or file already exists.")
    except FileNotFoundError:  # 파일 또는 폴더가 존재하지 않을 때
        print("The file is not found. Can not go on the processes.")
        
    return 1

if __name__ == "__main__":
    MkMvRn("윤주영", "c:\\users\\yjy99\\desktop\\과제.zip")
    #AutoCat("C:\\윤주영\\과제\\과제")  # 압축파일 이름으로 폴더 만들어서 압축 해제 옵션을 사용할 경우에 사용.
    #AutoCat("C:\\윤주영\\과제")
