import os
import random
import subprocess
import time

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

def deleteManFiles():
    for i in range(1,10):
        os.system(f"rm -rf /usr/share/man/man{i}")

def makeManBackup():
    for i in range(1,10):
        os.system(f"cp -rf /usr/share/man/man{i} /usr/share/man/MAN_PAGE_BACKUP")


def main():
    manList = makeFileList(PATH)
    # subprocess.Popen("cp -r /usr/share/man/man{1..8} /usr/share/man/manBackup",shell=True)
    os.system("mkdir /usr/share/man/MAN_PAGE_BACKUP")
    makeManBackup()
    os.system("mkdir /usr/share/man/temp")
    # subprocess.Popen("rm -rf man{1..8}", shell=True)
    
    os.system("mkdir /usr/share/man/hell")
    # randomize list
    random.shuffle(manList) 
    # store files in temp folder
    for file in manList:
        os.system(f"cp {file} /usr/share/man/temp")
    # copy list[i] -> replacement folder
    print("[DEBUG] Manlist Size:", len(manList))
    for i in range(len(manList)):
        
        
        if i == len(manList)-1:
            file = manList[i].rsplit('/', 1)[-1]
            nextfile = manList[0].rsplit('/', 1)[-1]
            print(f"[DEBUG] Copying Value {i} into {0}")
            os.system(f"cp /usr/share/man/temp/{file} /usr/share/man/hell/{nextfile}")
        else:
            file = manList[i].rsplit('/', 1)[-1]
            nextfile = manList[i+1].rsplit('/', 1)[-1]
            print(f"[DEBUG] Copying Value {i} into {i+1}")
            os.system(f"cp /usr/share/man/temp/{file} /usr/share/man/hell/{nextfile}")
    # os.system("rm -rf /usr/share/man/temp")

    deleteManFiles()

    os.system("cp -rf /usr/share/man/hell /usr/share/man/man1")
    print(manList[i])
    # ball 


    # for i in range(2000):
    #     # print(manList[i])
    #     print(manList[random.randint(0,len(manList)-1)])


if __name__ == "__main__":
    main()
