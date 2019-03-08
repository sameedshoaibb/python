import commands
output = commands.getoutput('ps -A')
services=['Suricata', 'blacklist', 'AccountingServi', 'charon','openvpn-tcp@server', 'openvpn-udp@server','iptables']
failed=[]

for i in services:
        if i=='Suricata':
                suricata_output_old = commands.getoutput('systemctl status suricata | grep "Active" ')
                suricata_output = suricata_output_old.strip()
                if suricata_output.startswith("Active: inactive (dead)"):
                        suricata_info_old= commands.getoutput('systemctl status suricata | grep "Loaded" ')
                        suricata_info = suricata_info_old.strip()
                        if not suricata_info.startswith("Loaded: loaded (/usr/lib/systemd/system/suricata.service; disabled") | suricata_output.startswith("Active: active (running)"):
                                failed.append('Suricata')
        elif i=='blacklist':

                blacklist_output_old = commands.getoutput('systemctl status blacklist | grep "Active" ')
                blacklist_output = blacklist_output_old.strip()
                if blacklist_output.startswith("Active: inactive (dead)"):
                        blacklist_info_old= commands.getoutput('systemctl status suricata | grep "Loaded" ')
                        blacklist_info = blacklist_info_old.strip()
                        if not blacklist_info.startswith("Loaded: loaded (/usr/lib/systemd/system/suricata.service; disabled") | blacklist_output.startswith("Active: active (running)"):
                                failed.append('blacklist')
        elif i=='iptables':
                iptables_output_old = commands.getoutput('systemctl status iptables | grep "Active:" ')
                iptables_output= iptables_output_old.strip()
                if not iptables_output.startswith("Active: inactive (dead)"):
                        failed.append('iptables')
        elif i=='openvpn-tcp@server':

                tcp_output_old = commands.getoutput('systemctl status openvpn-tcp@server | grep "Active" ')
                tcp_output = tcp_output_old.strip()
                if tcp_output.startswith("Active: inactive (dead)"):
                        tcp_info_old= commands.getoutput('systemctl status openvpn-tcp@server | grep "Loaded" ')
                        tcp_info = tcp_info_old.strip()
                        if not tcp_info.startswith("Loaded: loaded (/usr/lib/systemd/system/suricata.service; disabled"):
                                failed.append('openvpn-tcp@server')
                elif not tcp_output.startswith("Active: active (running)"):
                        failed.append('openvpn-tcp@server')
        elif i=='openvpn-udp@server':

                udp_output_old = commands.getoutput('systemctl status openvpn-udp@server | grep "Active" ')
                udp_output = udp_output_old.strip()
                if udp_output.startswith("Active: inactive (dead)"):
                        udp_info_old= commands.getoutput('systemctl status openvpn-udp@server | grep "Loaded" ')
                        udp_info = udp_info_old.strip()
                        if not udp_info.startswith("Loaded: loaded (/usr/lib/systemd/system/suricata.service; disabled"):
                                failed.append('openvpn-udp@server')
                elif not udp_output.startswith("Active: active (running)"):
                        failed.append('openvpn-udp@server')
        else:
                if not i in output:
                        failed.append(i)
if len(failed) == 0:
        print("Check Passed")
        exit(0)

else:
        print ', '.join(failed)
        exit(1)