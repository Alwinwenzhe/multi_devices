# -*- encoding=utf8 -*-
__author__ = "EDY"

from airtest.core.api import *

auto_setup(__file__)

# 程序执行异常就返回首页
def back_to_home():
    home = exists(Template(r"tpl1705982250612.png", record_pos=(0.001, 0.817), resolution=(1080, 1920)))
    a = 0
    while a<4:
        try:
            if home:
                print("找到首页元素，跳出循环")
                break
            elif home == False:
                keyevent("BACK")
                print("首页未找到，返回上一层")
        except:
            print("程序执行异常")
        a +=1