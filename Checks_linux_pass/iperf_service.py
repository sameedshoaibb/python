import json
import subprocess
import re
import time
import logging
import socket
import requests

logging.basicConfig(
	filename='/var/log/iperflogs.log',
	level=logging.DEBUG,
	format='%(asctime)s %(message)s',
	datefmt='%m/%d/%Y %I:%M:%S %p')

protocol = 'TCP'
port = 5201
parallel_sessions =	15
iteration_time = 14400
retry_timeout = 15
unit = "m"

def logme(log):
	logging.info(log)
	return True

def updateBenchmarkSpeed(nasidentifier, speed):
	url = ""
	querystring = {"token":"","u_id":"47","m":"1"}
	payload = {nasidentifier: speed}
	response = requests.request("POST", url, data=payload, params=querystring)
	return response.text

def getIperfServer(nasidentifier):
	url = ""
	querystring = {"sHost":nasidentifier}
	headers = {'x-psk': ""}
	response = requests.request("GET", url, headers=headers, params=querystring)
	if response.text:
		json_data = json.loads(response.text)
		if json_data['header']['code']==1:
			return json_data['body']['iperf']
		else:
			return False
	
def parseOutput(output):
	results = {}
	regex = r"([0-9]+.[0-9]+ [A-Z]bits\/sec)"	
	for line in output.split('\n'):
		if 'sender' in line.strip():
  			match = re.search(regex, line.strip())
  			if match:
  				sender_data = match.group(0).split()
				results['sender'] = sender_data[0]

  		if 'receiver' in line.strip():
  			match = re.search(regex, line.strip())
  			if match:
  				reciever_data = match.group(0).split()
				results['reciever'] = reciever_data[0]

	with open('/opt/sensu/embedded/bin/sensu-custom-checks/iperflog.py','w') as file:

        iperf_send = socket.gethostname()+'.iperf_test.'+'sender', results["sender"], epoch
        iperf_recieve = socket.gethostname()+'.iperf_test.'+'reciever', results["reciever"], epoch
        iperf_send_s=[]
        iperf_recieve_r=[]

        iperf_send_s.append("print" + " " + '"{} {} {}"'.format(iperf_send[0],iperf_send[1],iperf_send[2]))
        iperf_recieve_r.append("print" + " " + '"{} {} {}"'.format(iperf_recieve[0],iperf_recieve[1],iperf_recieve[2]))
        data1=file.write(str(iperf_send_s[0]))
        data_blank=file.write("\n")
        data2=file.write(str(iperf_recieve_r[0]))
        data_blank=file.write("\n")
        file.close()
        #a = socket.gethostname()+'.iperf_test.'+'sender', results["sender"], epoch
        print socket.gethostname()+'.iperf_test.'+'reciever', results["reciever"], epoch
        #print results["reciever"]

	return results


def startTest(retrycount=0):
	retrycount = retrycount + 1
	hostname 		= socket.gethostname()
	iperfServer 	= getIperfServer(hostname)
	logme("Running Test("+str(retrycount)+") - "+str(hostname)+" - "+str(iperfServer))
	if iperfServer!="":
		cmd = "iperf3 -c "+str(iperfServer)+" -p "+str(port)+" -f "+unit+" -P "+str(parallel_sessions)
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
		output, error = process.communicate()
		if 'iperf Done' in output:
			iperfResponse =  parseOutput(output)
			if iperfResponse is not None:
				logme(iperfResponse)
				logme(updateBenchmarkSpeed(hostname,iperfResponse['sender']))
		else:
			newtimeout = retry_timeout+retrycount
			logme("iperf server busy. retying in "+str(newtimeout))
			time.sleep(newtimeout)
			startTest(retrycount)
	else:
		logme("iperf server not found for host '"+str(hostname)+"'. retying in "+str(retry_timeout))
		time.sleep(retry_timeout)
		startTest(retrycount)

if __name__ == '__main__':
	while(True):
		startTest()
		logme("waiting (in seconds): "+str(iteration_time))
		time.sleep(iteration_time)
