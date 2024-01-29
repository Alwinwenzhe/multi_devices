# -*- encoding=utf-8 -*-
import subprocess
import datetime

def TestWait():
  print (datetime.datetime.now())
  p=subprocess.Popen("sleep 10",shell=True)
  p.wait()
  print (p.returncode)
  print (datetime.datetime.now())

TestWait()