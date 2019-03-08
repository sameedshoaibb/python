import commands
output = commands.getoutput('ps -A')
services=['Suricata','iptables','blacklist','AccountingService','named','iperftester','radiusd','squid']
failed=[]

for i in services:
	 if i=='squid':
	 	squid_output_old = commands.getoutput('systemctl status squid | grep "Active" ')
        squid_output = squid_output_old.strip()
        if squid_output.startswith("Active: inactive") | squid_output.startswith("Active: failed"):
            squid_info_old= commands.getoutput('systemctl status squid | grep "Loaded" ')
            squid_info = squid_info_old.strip()
            if not  squid_output.startswith("Active: active (running)") or squid_info.startswith("/usr/lib/systemd/system/squid.service; enabled"):
                failed.append('squid')

if len(failed) == 0:
        print("Check Passed")
        exit(0)

else:
        print ','.join(failed)
        exit(1)
