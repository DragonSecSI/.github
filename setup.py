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
    for subdirs, dirs, files in os.walk("."):
        for dirr in dirs:
            if "DCTF-chall" in dirr:
                print(dirr)
                return dirr

if __name__ == "__main__":
    init()
    challenge = file()
    if challenge:
        challenge+="/challenge.yml"
    else:
        challenge = "challenge.yml"
    print(challenge)
    os.system(f"ctf challenge sync '{challenge}';ctf challenge install '{challenge}'")
