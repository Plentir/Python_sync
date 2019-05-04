import os

def GetNameSubdir(dirs):
    name_subdirs = os.listdir(dirs)
    
    f = open("C:\\Users\\yjy99\\Desktop\\Subdirectories list.txt", "w")
    
    for line in name_subdirs:
        f.write("%s\n" %line)

    f.close()
    print("Done.")

    return 1


def GetNameAllSubdir(dirs):
    f = open("C:\\Users\\yjy99\\Desktop\\Name Subdirectories_All.txt", "w")

    for i in os.walk(dirs):
        name_subdir = i[0].split(dirs)[-1].split("\\")
        
        if i[0] is dirs:
            f.write("The list of a files in " + dirs + "\n\n")
            continue

        elif len(name_subdir) >= 3:  # 하위 폴더 반환
            f.write("%s└%s\n" %((" " * 3 * (len(i[0].split(dirs)) - 1)), name_subdir[-1]))
            
            for j in i[-1]:  # 폴더 내 파일 반환
                f.write("%s└%s\n" %((" " * 3 * len(i[0].split(dirs))), j))

        else:  # 최상위 폴더 반환
            f.write("%s\n" %(name_subdir[-1]))

            if len(i[-1]) != 0:
                for j in i[-1]:  # 폴더 내 파일 반환
                    f.write("%s└%s\n" %((" " * 3 * (len(i[0].split(dirs)) - 1)), j))
            
            else:
                continue
        
        f.write("\n")  # 디렉터리 변동 후 줄 바꿈

    f.close()
    print("Done.")

    return 1


if __name__ == "__main__":
    # GetNameSubdir("D:\\Media\\영상\\Movies\\해외 영화")
    GetNameAllSubdir("D:\\Media\\영상\\Movies\\해외 영화")