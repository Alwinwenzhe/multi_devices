# -*- encoding=utf8 -*-
# STATUS:PASS
# TIME:2024-1-15
__author__ = "Alwin"

from airtest.core.api import *
import time
import subprocess
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
using("jnt_999_utils.air")
using(r"j002_home.air")
from jnt_999_utils import *

from airtest.core.settings import Settings as ST
from utils.oper_gui import GuiFunction
auto_setup(__file__)
# ST.PROJECT_ROOT=r"D:\Scripts\Airtest\jnt"
ST.THRESHOLD = 0.9



# 用户协议
def agreement():
    sleep(3)
    agree = exists(Template(r"tpl1704942546705.png", record_pos=(-0.004, 0.048), resolution=(1260, 2800)))
    if agree:
        touch(Template(r"tpl1704942571072.png", record_pos=(-0.002, 0.179), resolution=(1260, 2800)))

def Login():
    sleep(3)
    # 点击一次，可能会触发输入法失败
    touch(Template(r"tpl1705553690764.png", record_pos=(-0.202, -0.187), resolution=(1080, 1920)),times=2)
    sleep(3)
    text("test21")
    touch(Template(r"tpl1705553702192.png", record_pos=(-0.192, 0.017), resolution=(1080, 1920)))
    text("lanhai888")
    try:
        touch(Template(r"tpl1705553711715.png", record_pos=(-0.382, 0.191), resolution=(1080, 1920)))
    except:
        pass
    touch(Template(r"tpl1702997098181.png", record_pos=(0.002, 0.203), resolution=(1260, 2800)))
    touch(assert_exists(Template(r"tpl1704161023187.png", record_pos=(-0.403, 1.083), resolution=(1260, 2800)), "登陆成功"))

def choose_input():
    sleep(1)
    touch(Template(r"tpl1710125933851.png", record_pos=(0.004, 0.076), resolution=(1080, 1920)))
    touch(wait(Template(r"tpl1710125978764.png", record_pos=(-0.173, 0.019), resolution=(1080, 1920))))
    sleep(1)
    swipe(Template(r"tpl1710126059393.png", record_pos=(-0.181, 0.807), resolution=(1080, 1920)), vector=[-0.1574, -0.736])
    sleep(1)
    touch(Template(r"tpl1710126690154.png", record_pos=(-0.274, 0.537), resolution=(1080, 1920)))
    touch(wait(Template(r"tpl1710126121404.png", record_pos=(-0.137, -0.408), resolution=(1080, 1920))))
    touch(wait(Template(r"tpl1710126175310.png", record_pos=(-0.32, -0.05), resolution=(1080, 1920))))
    sleep(1)
    touch(wait(Template(r"tpl1710126202983.png", record_pos=(-0.128, -0.026), resolution=(1080, 1920))))
    touch(wait(Template(r"tpl1710126286905.png", record_pos=(-0.215, -0.387), resolution=(1080, 1920))))
    keyevent("HOME")
    sleep(1)
    start_app("uni.UNI393E608")
    

def init_dev():
    '''
    有了它，每次运行前，就会自动连接虚拟机，不用先链接设备再测试了
    '''
    dev = connect_device("android://127.0.0.1:5037/127.0.0.1:16384?cap_method=ADBCAP&touch_method=MAXTOUCH&")
    auto_setup(__file__)
    

    
if __name__ == '__main__':
    choose_input()
    sleep(5)
    if exists(Template(r"tpl1709862093018.png", record_pos=(0.012, -0.119), resolution=(1080, 1920))):
        Login()
    else:
        print("已经登录，先退出，确保账号正确")
        touch(wait(Template(r"tpl1706507470094.png", record_pos=(0.403, 0.855), resolution=(1080, 1920))))
        touch(wait(Template(r"tpl1706507492490.png", record_pos=(-0.001, 0.569), resolution=(1080, 1920))))
        sleep(1)
        Login()
   





