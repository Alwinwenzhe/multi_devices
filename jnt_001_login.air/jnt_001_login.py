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
#     agreement()
#     sleep(2)
#     touch(Template(r"tpl1704727811404.png", record_pos=(0.356, 0.137), resolution=(1080, 1920)))

    sleep(1)
    touch(Template(r"tpl1705553690764.png", record_pos=(-0.202, -0.187), resolution=(1080, 1920)))

    text("test21")
    touch(Template(r"tpl1705553702192.png", record_pos=(-0.192, 0.017), resolution=(1080, 1920)))

    text("lanhai888")

    try:
        touch(Template(r"tpl1705553711715.png", record_pos=(-0.382, 0.191), resolution=(1080, 1920)))

    except:
        pass
    touch(Template(r"tpl1702997098181.png", record_pos=(0.002, 0.203), resolution=(1260, 2800)))
    touch(assert_exists(Template(r"tpl1704161023187.png", record_pos=(-0.403, 1.083), resolution=(1260, 2800)), "登陆成功"))


# start_app('uni.UNI393E608')
# time.sleep(3)

if __name__ == '__main__':

    try:
        log_interface = exists(Template(r"tpl1705553735432.png", record_pos=(-0.254, -0.086), resolution=(1080, 1920)))
        mine = exists(Template(r"tpl1706507406015.png", record_pos=(0.402, 0.858), resolution=(1080, 1920)))

        if log_interface:
            Login()
        elif mine:
            print("已经登录，先退出，确保账号正确")
            touch(wait(Template(r"tpl1706507470094.png", record_pos=(0.403, 0.855), resolution=(1080, 1920))))
            touch(wait(Template(r"tpl1706507492490.png", record_pos=(-0.001, 0.569), resolution=(1080, 1920))))
            sleep(1)
            Login()
    except:
        print("运行出错")




