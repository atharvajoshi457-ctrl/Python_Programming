import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to Create Folder")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for Log Files Gets Created Succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log File Gets Created with name : ",FileName)

    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System------\n")
    fobj.write("\tLog Created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("-------------------End of Log File----------------\n")
    fobj.write(Border+"\n")

    print("CPU Usage : ",psutil.cpu_percent())

def main():
    Border = "-"*50
    print(Border)
    print("-----Marvellous Platform Surveillance System------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h"or sys.argv[1] == "--H"):
            print("This script is used to :")
            print("1 : Create automatic logs")
            print("2 : Executes prediocally")
            print("3 : Sends mail with the Log")
            print("4 : Store information of the process")
            print("5 : Store information about cpu")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : Time in Minutes for periodic Scheduling")
            print("DirectoryName : Name the directory to create auto logs" )

        else:
            print("Unable to proceed there is no such option")
            print("please use --h,--u for more Details")
    
    # python Demo.py 5 marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects Logic")
        print("Time Interval :",sys.argv[1])
        print("Directory Name :",sys.argv[2])
        
        # Apply the Scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Surveillance System Started Succesfully")
        print("Directory Created with name : ",sys.argv[2])
        print("Time Interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to Stop the Execution")

        # Wait Till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of commandline Arguments")
        print("Unable to proceed there is no such option")
        print("please use --h,--u for more Details")

    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__ == "__main__":
    main()