import socket
import time
arr = []
def hostname(hostname):
    try:
        socket.gethostbyname(hostname)
        return 1
    except socket.error:
        return 0

for i in range(0,3):
    a = hostname('google.com')
    arr.append(a)
    print (arr)
    time.sleep(2)

if arr[0] == 1 and arr[1] == 1:
    print ("DNS is resolving")
else:
    print ("DNS is not resolving")
