import sys
import os
import time
import schedule        
            
def Fun(DirName):
    pass

def main():
    Border = "-"*50
    print(Border)
    print("-------Marvellous Data Shield System--------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h"or sys.argv[1] == "--H"):
            print("1 : Takes Auto Backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup prediocally")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print("ScriptName.py TimeInterval Source Directory")
            print("TimeInterval : Time in Minutes for periodic Scheduling")
            print("SourceDirectory : Name of directory to be backed up")

        else:
            print("Unable to proceed there is no such option")
            print("please use --h,--u for more Details")
    
    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects Logic")
        print("Time Interval :",sys.argv[1])
        print("Directory Name :",sys.argv[2])
        
        # Apply the Scheduler
        schedule.every(int(sys.argv[1])).minutes.do(Fun,sys.argv[2])

        print("Data Shield System Started Succesfully")
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