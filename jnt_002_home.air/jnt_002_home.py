# -*- encoding=utf8 -*-
# STATUS:PASS
# TIME:2024-1-15
__author__ = "Alwin"
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from airtest.core.api import *
from airtest.core.settings import Settings as ST
auto_setup(__file__)
ST.THRESHOLD = 0.8

## 切换测试项目 
def choose_test_pro():
    touch(Template(r"tpl1703296910243.png", record_pos=(-0.402, 1.079), resolution=(1260, 2800)))
    pro_test = exists(Template(r"tpl1704164392979.png", record_pos=(-0.103, -0.953), resolution=(1260, 2800)))
    if pro_test:
        print("当前项目就是测试项目")
    else:
        touch(Template(r"tpl1703213116524.png", record_pos=(-0.439, -0.95), resolution=(1260, 2800)))
        sleep(1)
        touch(Template(r"tpl1703213532858.png", record_pos=(-0.051, -0.519), resolution=(1260, 2800)))
        sleep(1)
        assert_exists(Template(r"tpl1703213564563.png", record_pos=(-0.133, -0.956), resolution=(1260, 2800)), "项目切换成功")

        
# 切换到考勤打卡项目
def choose_clock_pro():
    touch(Template(r"tpl1703296910243.png", record_pos=(-0.402, 1.079), resolution=(1260, 2800)))
    pro_clockin = exists(Template(r"tpl1704164927088.png", record_pos=(-0.128, -0.948), resolution=(1260, 2800)))
    if pro_clockin:
        print("当前项目就是办公人员考勤项目")
    else:
        touch(Template(r"tpl1703213116524.png", record_pos=(-0.439, -0.95), resolution=(1260, 2800)))
        sleep(1)
        touch(Template(r"tpl1704164974029.png", record_pos=(-0.287, 0.543), resolution=(1260, 2800)))
        sleep(1)

        assert_exists(Template(r"tpl1704164927088.png", record_pos=(-0.128, -0.948), resolution=(1260, 2800)), "项目切换成功")
        

# 考勤打卡
def clock_in():
    touch(Template(r"tpl1704685984704.png", record_pos=(-0.002, 1.04), resolution=(1260, 2800)))
    touch(Template(r"tpl1704685998853.png", record_pos=(-0.368, 0.358), resolution=(1260, 2800)))
    sleep(1)
    touch(wait(Template(r"tpl1703213377108.png", record_pos=(0.419, 0.915), resolution=(1260, 2800))))
    sleep(1)
    touch(Template(r"tpl1703213399888.png", record_pos=(0.002, 0.947), resolution=(1260, 2800)))
    sleep(1)
    assert_exists(Template(r"tpl1703326540959.png", record_pos=(0.005, 0.005), resolution=(1260, 2800)), "打卡成功")
    sleep(1)
    ## 回到工作台首页
    touch(Template(r"tpl1703213464719.png", record_pos=(-0.437, -0.952), resolution=(1260, 2800)))
    sleep(1)

# 测试项目信息查看
def check_project_info():
    touch(Template(r"tpl1703296885456.png", record_pos=(-0.039, -0.282), resolution=(1260, 2800)))
    sleep(1)
    
    assert_exists(Template(r"tpl1704166215895.png", record_pos=(-0.026, -0.063), resolution=(1260, 2800)), "验证项目信息")
    ### 验证导航
    touch(Template(r"tpl1704166283464.png", record_pos=(0.352, -0.168), resolution=(1260, 2800)))
    assert_exists(Template(r"tpl1705556181400.png", record_pos=(-0.07, 0.055), resolution=(1080, 1920)), "地图信息正确")
    touch(Template(r"tpl1704166590000.png", record_pos=(-0.436, -0.953), resolution=(1260, 2800)))
    touch(Template(r"tpl1704166610753.png", record_pos=(-0.438, -0.951), resolution=(1260, 2800)))
    
# 装备
def enter_equip():
    sleep(1)
    touch(Template(r"tpl1705040395886.png", record_pos=(0.174, -0.465), resolution=(1080, 1920)))
    wait(Template(r"tpl1705040842019.png", record_pos=(-0.019, -0.014), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1705042863674.png", record_pos=(0.006, 0.004), resolution=(1080, 1920)), "设备信息回显正确")
    touch(Template(r"tpl1705042888482.png", record_pos=(-0.436, -0.764), resolution=(1080, 1920)))
    

# 视频
def vedio_manager():
    sleep(1)
    touch(Template(r"tpl1705048895713.png", record_pos=(0.391, -0.104), resolution=(1080, 1920)))
    sleep(3)
    assert_exists(Template(r"tpl1705556235208.png", record_pos=(-0.154, -0.294), resolution=(1080, 1920)), "视频管理没有明显报错")
    touch(Template(r"tpl1705049220642.png", record_pos=(-0.434, -0.763), resolution=(1080, 1920)))





# 用例开始：
# 01--考勤打卡---模拟器中不能打卡
# choose_clock_pro()
# clock_in()
    
# 02--测试项目中，进行信息查看，回到首页
choose_test_pro()
check_project_info()

# 03--进入装备后，返回
enter_equip()
vedio_manager()




