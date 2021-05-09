import os
import re
import sys

def init():
    #change this:
    CTFD_TOKEN = sys.argv[1]
    #change this:
    CTFD_URL = "https://dctf.dragonsec.si"
    

    os.system(f"echo '{CTFD_URL}\n{CTFD_TOKEN}\ny' | ctf init")

def file():
    for subdirs, dirs, files in os.walk(".."):
        for dirr in dirs:
            print(dirr)
            if "DCTF-chall" in dirr:
                print(dirr)
                return dirr

if __name__ == "__main__":
    init()
    challenge = file()
    if not challenge:
        challenge="challenge.yml"
    print("this is what we sync: "+challenge)
    #challenge+="/challenge.yml"
    os.system(f"ls ../")
    #os.system(f"ctf challenge sync '{challenge}';ctf challenge install '{challenge}'")
