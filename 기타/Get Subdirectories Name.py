import os

def GetNameAllSubdir(dirs):  # 모든 하위 디렉터리의 목록을 텍스트 파일로 저장.
    dir_desktop = os.environ["USERPROFILE"] + "\\Desktop"
    dir_trg = dirs.split(sep="\\\\")[-1]
    f = open("%s\\File list_%s.txt" %(dir_desktop, dir_trg), "w", encoding="utf-8")

    for i in os.walk(dirs):
        name_subdir = i[0].split(dirs)[-1].split("\\")
        
        if i[0] is dirs:
            f.write("The list of files in " + dirs + "\n" + 60*"=" + "\n\n")
            continue

        elif len(name_subdir) >= 3:  # 하위 폴더 반환
            f.write("%s└ [dir] %s\n" %((" " * 3 * (len(name_subdir) - 2)), name_subdir[-1]))
            
            for j in i[-1]:  # 폴더 내 파일 반환
                f.write("%s└ %s\n" %((" " * 3 * (len(name_subdir) - 1)), j))

        else:  # 최상위 폴더 반환
            f.write("[dir] %s\n" %(name_subdir[-1]))

            if len(i[-1]) != 0:
                for j in i[-1]:  # 폴더 내 파일 반환
                    f.write("%s└ %s\n" %((" " * 3 * (len(name_subdir) - 1)), j))
            
            else:
                continue
        
        #f.write("\n")  # 디렉터리 변경 후 줄 바꿈

    f.close()
    print("The report file is created in %s." %dir_desktop)

    return 1


if __name__ == "__main__":
    trg = input("파일 목록을 작성할 디렉터리를 입력하세요.\n입력: ")
    GetNameAllSubdir(trg)
