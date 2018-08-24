
#set username & password

import subprocess
import os
import time
import paramiko
import re


timestr =time.asctime( time.localtime(time.time()) )
a=subprocess.check_output(['hostname'])
save_path = '/home/sameed/Pictures/logs'
completeName = os.path.join(save_path,a+".txt")
path= '/public_html/Tap-Adapter'
ftp_path= os.path.join(path,a+".txt")

def kaam():
	print 
	
	completeName = os.path.join(save_path,a+".txt")        

	process = subprocess.check_output(['hostname','-I'])   #process = process.strip()
	final_process = []
	final_process = re.findall(r'\S+', process)
	for pro in final_process:
		print pro+" This is pro"
		res = subprocess.call(["ping","-I",pro,"8.8.8.8","-c","1"])
		if res == 0:   
			f = open(completeName,'a')
			f.write(timestr + ' ' + '-->'+ '')
			f.write('ping from {} to 8.8.8.8 is OK 1\n'.format(pro))
			f.close()
		else:
			f = open(completeName,'a')
			f.write('ping from {} to 8.8.8.8 is FAILED \n'.format(pro))
			f.close()
	print "Transfering the file. please wait"

def error():
	print "There is an error", e
	
try:	
	kaam()
except Exception as e:
	error()
else:
	print "Perfecto!!"

try:	
	ssh_client =paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname='',username='',password="")
	ftp_client=ssh_client.open_sftp()
except Exception as e:
	print "The error is",e
	print "error in opening sftp"
else:		
	ftp_client.put(completeName,ftp_path)
	ftp_client.close()
	print "Written content in the file successfully"

