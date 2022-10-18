import os
import random
import subprocess

ROOTS = [f"man{i}" for i in range(1,9)]

def main():
    manList = list()
    mixedManList = list()
    # subprocess.Popen("cp -r /usr/share/man/man8 /usr/share/man/man8backup",shell=True)
    for root, dirs, files in os.walk(f"/usr/share/man/", topdown=True):
        rootpath = root.split("/")
        if rootpath[4] in ROOTS:
            for name in files:
                # print(os.path.join(root, name))
                manList.append(os.path.join(root,name))
                mixedManList.append(os.path.join(root,name))

    
    # for i in range(2000):
    #     # print(manList[i])
    #     print(manList[random.randint(0,len(manList)-1)])


if __name__ == "__main__":
    main()
