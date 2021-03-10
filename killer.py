import psutil
import time

def pauseAndResumeProcess(process_pid):
    p = psutil.Process(process_pid)
    p.suspend()
    time.sleep(3)
    p.resume()

def findProcessIdByName(processName):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects;

while True: 
    processes = findProcessIdByName('zoom')
    for process in processes:
        pauseAndResumeProcess(process['pid'])


