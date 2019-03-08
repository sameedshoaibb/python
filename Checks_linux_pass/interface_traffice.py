#!/bin/python
"""
@developer sameed
@date: April 2019
"""

import time
import subprocess
import socket
epoch = int(time.time())

try:
  defaultInterfaceData = subprocess.Popen("cat /proc/net/dev | grep $(/sbin/ip route | awk '/default/ { print $5 }')", shell=True, stdout=subprocess.PIPE)
  defaultInterface = defaultInterfaceData.stdout.readline().strip()
  data = defaultInterface.split()
  RX_BYTES    = data[1]
  RX_PACKETS  = data[2]
  RX_ERRORS  = data[3]
  RX_DROPS  = data[4]

  TX_BYTES    = data[9]
  TX_PACKETS  = data[10]
  TX_ERRORS  = data[11]
  TX_DROPS  = data[12]

  print socket.gethostname()+'.default_interface.'+'rxBytes', RX_BYTES, epoch
  print socket.gethostname()+'.default_interface.'+'rxPackets', RX_PACKETS, epoch
  print socket.gethostname()+'.default_interface.'+'rxErrors', RX_ERRORS, epoch
  print socket.gethostname()+'.default_interface.'+'rxDrops', RX_DROPS, epoch
  print socket.gethostname()+'.default_interface.'+'txBytes', TX_BYTES, epoch
  print socket.gethostname()+'.default_interface.'+'txPackets', TX_PACKETS, epoch
  print socket.gethostname()+'.default_interface.'+'txErrors', TX_ERRORS, epoch
  print socket.gethostname()+'.default_interface.'+'txDrops', TX_DROPS, epoch
except:
  print 'something went wrong'

exit(0)
