import commands
output = commands.getoutput('ps -A')
services=['Suricata','iptables','blacklist','AccountingService','named','iperftester']
failed=[]

for i in services:
	 if i=='iperftester':
	 	iperftester_output_old = commands.getoutput('systemctl status iperftester | grep "Active" ')
        iperftester_output = iperftester_output_old.strip()
        if iperftester_output.startswith("Active: inactive") | iperftester_output.startswith("Active: failed"):
            iperftester_info_old= commands.getoutput('systemctl status iperftester | grep "Loaded" ')
            iperftester_info = iperftester_info_old.strip()
            if not  iperftester_output.startswith("Active: active (running)") or iperftester_info.startswith("Loaded: loaded (/etc/systemd/system/iperftester.service; enabled"):
                failed.append('iperftester')

if len(failed) == 0:
        print("Check Passed")
        exit(0)

else:
        print ','.join(failed)
        exit(1)
