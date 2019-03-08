import commands
output = commands.getoutput('ps -A')
services=['Suricata','iptables','blacklist','AccountingService','named','iperftester','radius']
failed=[]

for i in services:
	 if i=='radius':
	 	radius_output_old = commands.getoutput('systemctl status radius | grep "Active" ')
        radius_output = radius_output_old.strip()
        if radius_output.startswith("Active: inactive") | radius_output.startswith("Active: failed"):
            radius_info_old= commands.getoutput('systemctl status radius | grep "Loaded" ')
            radius_info = radius_info_old.strip()
            if not  radius_output.startswith("Active: active (running)") or radius_info.startswith("Loaded: loaded (/usr/lib/systemd/system/radiusd.service; enabled"):
                failed.append('radius')

if len(failed) == 0:
        print("Check Passed")
        exit(0)

else:
        print ','.join(failed)
        exit(1)
