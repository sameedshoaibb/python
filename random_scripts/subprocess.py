#!/usr/bin/python
#From Where i took inspiration: https://pythonspot.com/python-subprocess/ & https://www.pythonforbeginners.com/os/subprocess-for-system-administrators

import sys
import subprocess
import time
import socket
import newrelic.agent

application = newrelic.agent.register_application(timeout=10)

@newrelic.agent.background_task()
def strongswanCount():
    proc1 = subprocess.Popen(['/usr/local/sbin/ipsec', 'status'], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', 'ESTABL'], stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc3 = subprocess.Popen(['grep', '-v', 'L2TP-PSK'], stdin=proc2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc4 = subprocess.Popen(['wc', '-l'], stdin=proc3.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1.stdout.close()
    proc2.stdout.close()
    proc3.stdout.close()

    (out, err) = proc4.communicate()
    count = out.strip()
    name="Custom/strongswan"
    newrelic.agent.record_custom_metric(name, int(count), application=application)


def ipsecCount():
    proc1 = subprocess.Popen(['/usr/local/sbin/ipsec', 'status'], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', 'ESTABL'], stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc3 = subprocess.Popen(['grep', '-v', 'L2TP-PSK'], stdin=proc2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc4 = subprocess.Popen(['grep', 'IPSec'], stdin=proc3.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc5 = subprocess.Popen(['wc', '-l'], stdin=proc4.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1.stdout.close()
    proc2.stdout.close()
    proc3.stdout.close()
    proc4.stdout.close()

    (out, err) = proc5.communicate()
    count = out.strip()
    name="Custom/ipsec"
    newrelic.agent.record_custom_metric(name, int(count), application=application)

def ikev2Count():
    proc1 = subprocess.Popen(['/usr/local/sbin/ipsec', 'status'], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', 'ESTABL'], stdin=proc1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc3 = subprocess.Popen(['grep', '-v', 'L2TP-PSK'], stdin=proc2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc4 = subprocess.Popen(['grep', 'IKEv2'], stdin=proc3.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc5 = subprocess.Popen(['wc', '-l'], stdin=proc4.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1.stdout.close()
    proc2.stdout.close()
    proc3.stdout.close()
    proc4.stdout.close()

    (out, err) = proc5.communicate()
    count = out.strip()
    name="Custom/ikev2"
    newrelic.agent.record_custom_metric(name, int(count), application=application)

if __name__ == "__main__":
    strongswanCount()
    ikev2Count()
    ipsecCount()
