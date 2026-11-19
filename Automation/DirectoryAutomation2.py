import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
    Ret = False
    
    Ret = os.path.exists(DirName)
    
    if(Ret == False):
        print("There is no such Directory")
        return
    
    Ret = os.path.isdir(DirName)
    
    if(Ret == False):
        print("It is not a Directory")
        return
    
    for FoldeName,SubFolder,FileName in os.walk(DirName):
        for fname in FileName:
            print("File name : ",fname)
            print("FIle Size : ",os.path.getsize(fname))    #Path issue
    
    

def main():
    Border = "-"*50
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)
    
    if(len(sys.argv) != 2):
        print("Invalid Number of Arguments ")
        print("Please specify the name of directory")
        return
    DirectoryScanner(sys.argv[1])
    
if __name__ == "__main__":
    main()