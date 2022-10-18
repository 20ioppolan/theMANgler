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
    mixedManList = list()
    # subprocess.Popen("cp -r /usr/share/man/man{1..8} /usr/share/man/manBackup",shell=True)
    subprocess.Popen("mkdir /usr/share/man/MAN_PAGE_BACKUP;cp -r /usr/share/man/man{1..8} /usr/share/man/MAN_PAGE_BACKUP", shell=True)
    # subprocess.Popen("rm -rf man{1..8}", shell=True)
    for file in manList:
        subprocess.Popen(f"cp {file} man1", shell=True)
        
    

    
    for i in range(2000):
        # print(manList[i])
        print(manList[random.randint(0,len(manList)-1)])


if __name__ == "__main__":
    main()
