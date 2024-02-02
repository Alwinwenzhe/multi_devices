# -*- encoding=utf8 -*-
__author__ = "Alwin"
# STATUS:PASS
# TIME:2024-1-15

import time
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from airtest.core.api import *
from airtest.core.settings import Settings as ST
ST.THRESHOLD = 0.8

auto_setup(__file__)


## 上传照片
def upload_photos():
    sleep(1)
    touch(wait(Template(r"tpl1703208643754.png", record_pos=(-0.001, 0.868), resolution=(1260, 2800))))
    sleep(3)
    touch(wait(Template(r"tpl1705285745925.png", record_pos=(0.123, -0.316), resolution=(1080, 1920))))
    sleep(1)
    touch(Template(r"tpl1703138560459.png", record_pos=(0.374, -0.946), resolution=(1260, 2800)))
    flag = True
    while flag:
        loading = exists(Template(r"tpl1706152138006.png", record_pos=(-0.002, 0.091), resolution=(1080, 1920)))
        if loading:
            print("正在上传中，请稍等！")
            sleep(2)
        else:
            flag = False
            print("上传完成")
    

## 选择维修物料
def choose_material():
    touch(Template(r"tpl1704175053849.png", record_pos=(-0.177, 0.158), resolution=(1260, 2800)))
    sleep(2)
    touch(wait(Template(r"tpl1704175072252.png", record_pos=(-0.05, 0.289), resolution=(1260, 2800))))
    sleep(1)
    # text("DECK",enter=False)
    shell('am broadcast -a INPUT_TEXT --es text "DECK"')
    touch(Template(r"tpl1704175195695.png", record_pos=(0.431, 0.289), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1704175427507.png", record_pos=(-0.199, 0.275), resolution=(1260, 2800)))
    # text("3",enter=False)
    shell('am broadcast -a INPUT_TEXT --es text "3"')
     
    
    
## 选择开始时间
def choose_start_time():
    ### 时间前推一天
    sleep(2)
    left_time = exists(Template(r"tpl1705287723572.png", record_pos=(-0.358, 0.089), resolution=(1080, 1920)))
    up_time = exists(Template(r"tpl1705236723951.png", record_pos=(-0.428, 0.034), resolution=(1080, 1920)))
    if left_time:
        touch(Template(r"tpl1705287723572.png", record_pos=(-0.358, 0.089), resolution=(1080, 1920)))
    elif up_time:
        touch(Template(r"tpl1705236723951.png", record_pos=(-0.428, 0.034), resolution=(1080, 1920)))
    else:
        raise Exception
    sleep(1)
    touch(Template(r"tpl1704176808593.png", record_pos=(0.198, 0.821), resolution=(1260, 2800)))
    wait(Template(r"tpl1704176828417.png", record_pos=(0.008, 0.811), resolution=(1260, 2800)))
    touch(Template(r"tpl1704176835907.png", record_pos=(0.337, 0.809), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703138320312.png", record_pos=(-0.001, 0.998), resolution=(1260, 2800)))
    sleep(1)
    
    
## 保养中的操作内容和保养拍照
def maintenance_photo(cur_date):
    touch(Template(r"tpl1704181706146.png", record_pos=(-0.136, 0.358), resolution=(1260, 2800)))
    shell('am broadcast -a INPUT_TEXT --es text "保养内容是自动化输入的内容，输入日期：{0}。"'.format(current_date))
    sleep(1)
    touch(Template(r"tpl1705556885852.png", record_pos=(-0.203, 0.713), resolution=(1080, 1920)))
    upload_photos()


# 第一个装备的维修，执行完成后回到装备首页
def repair(cur_date):
    if exists(Template(r"tpl1704187432995.png", record_pos=(-0.002, -0.158), resolution=(1260, 2800))):
        touch(Template(r"tpl1705108069090.png", record_pos=(-0.356, -0.068), resolution=(1080, 1920)))

    else:
        sleep(10)
        touch(Template(r"tpl1705108069090.png", record_pos=(-0.356, -0.068), resolution=(1080, 1920)))
    touch(Template(r"tpl1704167742228.png", record_pos=(0.003, 1.044), resolution=(1260, 2800)))
    ### 维修时间前推一天
    sleep(2)
    touch(wait(Template(r"tpl1704167798750.png", record_pos=(-0.042, -0.59), resolution=(1260, 2800))))
    choose_start_time()
    ### 领用拍照
    sleep(1)
    touch(Template(r"tpl1704180009597.png", record_pos=(-0.086, -0.148), resolution=(1260, 2800)))
    upload_photos()

    ### 维修物料选择
    sleep(2)
    choose_material()
    ###添加明细，并删除
    sleep(1)
    touch(Template(r"tpl1704175537776.png", record_pos=(0.008, 0.416), resolution=(1260, 2800)))
    touch(wait(Template(r"tpl1704175593042.png", record_pos=(0.387, 0.411), resolution=(1260, 2800))))
    sleep(1)
    
    swipe(Template(r"tpl1705286540197.png", record_pos=(-0.34, 0.823), resolution=(1080, 1920)), vector=[-0.0514, -0.8241])

    ### 维修部件
    touch(Template(r"tpl1704175855026.png", record_pos=(-0.153, 0.157), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1704175875236.png", record_pos=(0.411, 0.446), resolution=(1260, 2800)))
    sleep(1)
    ### 维修内容
    touch(Template(r"tpl1705331646959.png", record_pos=(-0.129, 0.131), resolution=(1080, 1920)))
    shell('am broadcast -a INPUT_TEXT --es text "维修内容是自动化输入的内容，输入日期：{0}。"'.format(current_date))

    ### 维修拍照
    sleep(1)
    touch(Template(r"tpl1704179916300.png", record_pos=(-0.079, 0.64), resolution=(1260, 2800)))
    upload_photos()
    sleep(2)
    swipe(Template(r"tpl1705289312127.png", record_pos=(-0.002, 0.793), resolution=(1080, 1920)), vector=[-0.274, -0.5962])

    touch(Template(r"tpl1703138574669.png", record_pos=(0.003, 1.03), resolution=(1260, 2800)))
    sleep(2)
    assert_exists(Template(r"tpl1704178331121.png", record_pos=(0.003, -0.773), resolution=(1260, 2800)), "维修数据添加正确")
    touch(Template(r"tpl1703212531617.png", record_pos=(-0.435, -0.95), resolution=(1260, 2800)))
    sleep(1)
    

    
# 保养，执行完成后回到装备首页
def maintenance(cur_date):
    if exists(Template(r"tpl1704187432995.png", record_pos=(-0.002, -0.158), resolution=(1260, 2800))):
        sleep(1)
        touch(Template(r"tpl1705466131618.png", record_pos=(-0.114, -0.17), resolution=(1080, 1920)))
    else:
        sleep(10)
        touch(Template(r"tpl1705466131618.png", record_pos=(-0.114, -0.17), resolution=(1080, 1920)))
    sleep(1)
    touch(wait(Template(r"tpl1704178695015.png", record_pos=(-0.194, -0.459), resolution=(1260, 2800))))
    
    touch(wait(Template(r"tpl1704178720818.png", record_pos=(-0.001, 1.044), resolution=(1260, 2800))))
    snapshot(msg="只是看看保养时间.")
    ## 物料信息
    ### 领用拍照
    touch(wait(Template(r"tpl1704180111941.png", record_pos=(-0.068, -0.271), resolution=(1260, 2800))))
    upload_photos()
    sleep(2)
    ### 选择物料
    choose_material()
    ### 保养
    swipe(Template(r"tpl1705289521802.png", record_pos=(-0.336, 0.698), resolution=(1080, 1920)), vector=[-0.0159, -0.7536])
    sleep(1)
    maintenance_photo(cur_date)
    sleep(1)
    swipe(Template(r"tpl1704187751963.png", record_pos=(-0.356, 0.89), resolution=(1260, 2800)), Template(r"tpl1704187774395.png", record_pos=(-0.367, -0.152), resolution=(1260, 2800)))

    touch(Template(r"tpl1704181902877.png", record_pos=(0.0, 0.896), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1704181916510.png", record_pos=(0.387, 0.833), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1704181943439.png", record_pos=(0.0, 1.029), resolution=(1260, 2800)))
    sleep(1)
    assert_exists(Template(r"tpl1705589545693.png", record_pos=(-0.011, -0.629), resolution=(1080, 1920)), "新增保养成功")
    touch(Template(r"tpl1704188006673.png", record_pos=(-0.435, -0.953), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1704188006673.png", record_pos=(-0.435, -0.953), resolution=(1260, 2800)))
    sleep(1)
    
# 开始执行用例
touch(Template(r"tpl1704167318084.png", record_pos=(-0.403, 1.077), resolution=(1260, 2800)))
touch(Template(r"tpl1704167324614.png", record_pos=(0.178, -0.282), resolution=(1260, 2800)))
sleep(5)
current_date = time.strftime("%Y-%m-%d") 
repair(current_date)
maintenance(current_date)
# 执行完成后，回到首页
sleep(1)
touch(Template(r"tpl1704692927039.png", record_pos=(-0.428, -0.95), resolution=(1260, 2800)))


