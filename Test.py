# Import module
import wmi, time
  
# Initializing the wmi constructor
f = wmi.WMI()
  
flag = 0
  
# Iterating through all the running processes
while True:
    for process in f.Win32_Process():
        if "RDR2.exe" == process.Name:
            flag = 1
            time.sleep(2)
            
    if flag == 0:
        print("Game is closed")