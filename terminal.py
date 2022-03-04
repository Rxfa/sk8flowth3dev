import re
import subprocess
result = subprocess.run(['powershell', '-c', 'Get-WmiObject win32_service | where {$_.name -eq "<name>"}'], stdout=subprocess.PIPE)
result.stdout
#print(result)
#pid_ = re.findall('ProcessID')

tr  = str(result)
tr = tr.split('\\n')
for i in tr: 
    pid_ = re.findall('ProcessId',i)
    
    if len(pid_)>0: 
        _pid = i[-7:-2]
        print(f"PID is {i[-7:-2]}")
        break
    else:
        _pid = 'NO PID found'

print(f"PID is {_pid}")