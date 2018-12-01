import sys
import os

def checkdir():
    if (os.getcwd() != "example"):
        os.chdir("/Users/cameron/Desktop/example")
        print("Running in, " + os.getcwd())
    else:
        print("running in, " + os.getcwd())
def write():
    checkdir()
    f = open("hackathon", "w")
    f.write("Hello World")
    f.close();
    
write()

