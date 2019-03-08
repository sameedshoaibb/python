import commands
output = commands.getoutput('ps -A')
services=['Suricata','iptables']
failed=[]

for i in services:
        if i=='Suricata':
                suricata_output_old = commands.getoutput('systemctl status suricata | grep "Active" ')
                suricata_output = suricata_output_old.strip()
                if suricata_output.startswith("Active: inactive (dead)") | suricata_output.startswith("Active: failed"):
                        suricata_info_old= commands.getoutput('systemctl status suricata | grep "Loaded" ')
                        suricata_info = suricata_info_old.strip()
                        if not suricata_info.startswith("Loaded: loaded (/usr/lib/systemd/system/suricata.service; disabled") | suricata_output.startswith("Active: active (running)"):
                                failed.append('Suricata')
        elif i=='iptables':
                iptables_output_old = commands.getoutput('systemctl status iptables | grep "Active:" ')
                iptables_output= iptables_output_old.strip()
                if not iptables_output.startswith("Active: active (exited)"):
                        failed.append('iptables')

        else:
                if not i in output:
                        failed.append(i)
if len(failed) == 0:
        print("Check Passed")
        exit(0)

else:
        print ','.join(failed)
        exit(1)
