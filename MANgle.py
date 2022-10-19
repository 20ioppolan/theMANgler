import os
import random
import subprocess

ROOTS = [f"man{i}" for i in range(1,9)]
PATH = "/usr/share/man/"

def makeFileList(path):
    manList = list()
    for root, dirs, files in os.walk(f"{path}", topdown=True):
            rootpath = root.split("/")
            if rootpath[4] in ROOTS:
                for name in files:
                    manList.append(os.path.join(root,name))
    return manList


def main():
    manList = makeFileList(PATH)
    shuffledManList = list()
    # subprocess.Popen("cp -r /usr/share/man/man{1..8} /usr/share/man/manBackup",shell=True)
    os.system("mkdir /usr/share/man/MAN_PAGE_BACKUP;cp -rf /usr/share/man/man{1..8} /usr/share/man/MAN_PAGE_BACKUP;mkdir /usr/share/man/temp")
    # subprocess.Popen("rm -rf man{1..8}", shell=True)
    
        
    
    os.system("mkdir usr/share/man/hell")
    # randomize list
    shuffledManList = random.shuffle(manList) 
    # store files in temp folder
    for file in manList:
        os.system(f"cp {file} /usr/share/man/temp")
    # copy list[i] -> replacement folder
    for i in range(len(shuffledManList)):
        if i == len(shuffledManList):
            os.system(f"cp /usr/share/man/temp/{shuffledManList[i]} /usr/share/man/hell/{shuffledManList[0]}")
        else:
            os.system(f"cp /usr/share/man/temp/{shuffledManList[i]} /usr/share/man/hell/{shuffledManList[i+1]}")
    # delete from temp folder
    os.system("rm -rf /usr/share/man/temp")
    # move to man 1 (or disperse around 9)
    os.system("rm -rf /usr/share/man/man{1..8}")
    os.system("cp -rf /usr/share/man/hell /usr/share/man/man1")

    # ball 


    # for i in range(2000):
    #     # print(manList[i])
    #     print(manList[random.randint(0,len(manList)-1)])


if __name__ == "__main__":
    main()
