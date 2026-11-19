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
    
    FileCount = 0
    EmptyFileCount = 0
    
    for FolderName,SubFolder,FileName in os.walk(DirName):
        for fname in FileName:
            FileCount = FileCount + 1
            
            fname = os.path.join(FolderName,fname)
            print("File name : ",fname)
            print("FIle Size : ",os.path.getsize(fname))   
            
            if(os.path.getsize(fname) == 0):        # Empty file
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)
    
    Border = "-"*50
    print(Border)
    print("----------------Automation Report ----------------")
    print("Total Files Scanned : ",FileCount)
    print("Empty File Count : ",EmptyFileCount)
    print(Border)

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
    
    print(Border)
    print("---------Marvellous Directory Automation----------")
    print(Border)
    
if __name__ == "__main__":
    main()