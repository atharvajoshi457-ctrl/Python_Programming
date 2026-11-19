import hashlib
import os



def CalculateChecksum(FileName):            # 4567
    fobj = open(FileName,"rb")
    
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1024)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
        
    fobj.close()
    
    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):
    Ret = False
    
    Ret = os.path.exists(DirectoryName)
    
    if(Ret == False):
        print("There is no such Directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    
    if(Ret == False):
        print("It is not a Directory")
        
    Duplicate = {}
        
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)
            
            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]
                
    return Duplicate
def DisplayResult(MyDict):
    
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))
    
    Count = 0
    
    for value in Result:
        for subvalue in value:
            Count = Count+1
            print(subvalue)
        print("Value of count is : ",Count)
        Count = 0
    
def main():
    
    Ret = FindDuplicate()
    DisplayResult(Ret)
    
if __name__ == "__main__":
    main()