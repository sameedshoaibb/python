import commands
output = commands.getoutput('ps -A')
services=['Suricata','iptables','blacklist','AccountingService','named']
failed=[]

for i in services:
	if i=='named':
		named_output_old = commands.getoutput('systemctl status named | grep "Active" ')
		named_output = named_output_old.strip()
    	if named_output.startswith("Active: inactive") | named_output.startswith("Active: failed"):
	        named_info_old = commands.getoutput('systemctl status named | grep "Loaded" ')
	        named_info = named_info_old.strip()
        	if not  named_output.startswith("Active: active (running)") or named_info.startswith("Loaded: loaded (/usr/lib/systemd/system/named.service; enabled"):
                failed.append('named')
	 

if len(failed) == 0:
        print("Check Passed")
        exit(0)

else:
        print ','.join(failed)
        exit(1)
