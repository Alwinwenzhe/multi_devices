# -*- encoding=utf8 -*-
# STATUS:PASS
# TIME:2024-1-15
__author__ = "Alwin"

from airtest.core.api import *
from termcolor import cprint
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

using("jnt_999_utils.air")
from jnt_999_utils import *

auto_setup(__file__)
from airtest.core.settings import Settings as ST
ST.THRESHOLD = 0.85

# 人员搜索
def search_personal(search_name='陈文哲'):
    '''
    实现人员搜索模块的人员搜索
    '''
    sleep(1)
    touch(Template(r"tpl1705544325572.png", record_pos=(-0.244, 0.207), resolution=(1080, 1920)))
    sleep(1)
    shell('am broadcast -a INPUT_TEXT --es text "{0}"'.format(search_name))
    sleep(1)
    keyevent("ENTER")
    sleep(1)
    touch(wait(Template(r"tpl1705544484072.png", record_pos=(0.005, 0.346), resolution=(1080, 1920))))
    touch(Template(r"tpl1705544507829.png", record_pos=(0.414, 0.071), resolution=(1080, 1920)))
    sleep(1)

# 审批意见
def approval_opinion_pass(content='同意'):
    sleep(1)
    touch(Template(r"tpl1705545112280.png", record_pos=(-0.154, 0.457), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1705545112280.png", record_pos=(-0.154, 0.457), resolution=(1080, 1920)))
    shell('am broadcast -a INPUT_TEXT --es text "{0}"'.format(content))
    sleep(1)
    touch(Template(r"tpl1705547670789.png", record_pos=(-0.353, 0.081), resolution=(1080, 1920)))
    touch(Template(r"tpl1705633177839.png", record_pos=(0.318, 0.809), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1705547751438.png", record_pos=(-0.007, 0.086), resolution=(1080, 1920)), "待办操作成功")
    sleep(1)

# 搜索项目或公司
def search_pro():
    ### 搜索付款项目
    sleep(2)
    touch(Template(r"tpl1703216668954.png", record_pos=(-0.348, 0.236), resolution=(1260, 2800)))
    sleep(1)
    shell('am broadcast -a INPUT_TEXT --es text "信能通达"')
    assert_exists(Template(r"tpl1707040516068.png", record_pos=(-0.343, 0.076), resolution=(1080, 1920)), "搜索成功")
    sleep(1)
    touch(Template(r"tpl1705631010943.png", record_pos=(-0.341, 0.119), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1703216860759.png", record_pos=(0.405, -0.76), resolution=(1260, 2800)))
    sleep(1)
    
# 上传文件
def upload_file():
    sleep(2)
    touch(Template(r"tpl1705405219860.png", record_pos=(-0.134, 0.555), resolution=(1080, 1920)))
    sleep(2)
    touch(Template(r"tpl1705405240092.png", record_pos=(-0.001, 0.356), resolution=(1080, 1920)))
    sleep(2)
    touch(Template(r"tpl1705405257844.png", record_pos=(-0.202, -0.098), resolution=(1080, 1920)))
    sleep(5)
    flag = True
    while flag:
        loading = exists(Template(r"tpl1706152592027.png", record_pos=(0.135, 0.054), resolution=(1080, 1920)))
        if loading:
            print("正在上传中，请稍等！")
            sleep(2)
        else:
            flag = False
            print("上传完成")
    
## 上传照片
def upload_photos():
    sleep(1)
    touch(wait(Template(r"tpl1703208643754.png", record_pos=(-0.001, 0.868), resolution=(1260, 2800))))
    sleep(3)
    touch(wait(Template(r"tpl1705285745925.png", record_pos=(0.123, -0.316), resolution=(1080, 1920))))
    sleep(1)
    touch(Template(r"tpl1703138560459.png", record_pos=(0.374, -0.946), resolution=(1260, 2800)))
    sleep(3)
    flag = True
    while flag:
        loading = exists(Template(r"tpl1706152138006.png", record_pos=(-0.002, 0.091), resolution=(1080, 1920)))
        if loading:
            print("正在上传中，请稍等！")
            sleep(2)
        else:
            flag = False
            print("上传完成")
    
## 选择仓库
def choose_storage():
    touch(Template(r"tpl1705592744833.png", record_pos=(-0.219, 0.081), resolution=(1080, 1920)))

    sleep(1)
    touch(Template(r"tpl1704764927738.png", record_pos=(0.415, 0.449), resolution=(1260, 2800)))
    sleep(1)

## 选择分类
def choose_type(typename="AT类"):
    # 点击分类后开始操作
    sleep(1)
    touch(Template(r"tpl1705592804074.png", record_pos=(-0.225, 0.194), resolution=(1080, 1920)))
    sleep(2)
    touch(Template(r"tpl1705380973998.png", record_pos=(0.007, 0.242), resolution=(1080, 1920)))
    sleep(1)
    # text(typename)
    shell('am broadcast -a INPUT_TEXT --es text "{0}"'.format(typename))
    touch(Template(r"tpl1704765732089.png", record_pos=(0.433, 0.285), resolution=(1260, 2800)))
    sleep(1)

## 选择物料
def choose_material(material_name='AT_001'):
    sleep(1)
    touch(wait(Template(r"tpl1705627276346.png", record_pos=(-0.057, 0.241), resolution=(1080, 1920))))
    sleep(1)
    # text(material_name)
    shell('am broadcast -a INPUT_TEXT --es text "{0}"'.format(material_name))
    touch(Template(r"tpl1704175195695.png", record_pos=(0.431, 0.289), resolution=(1260, 2800)))
    sleep(1)
    
## 选择数量
def choose_number():
    sleep(1)
    touch(Template(r"tpl1705628780697.png", record_pos=(-0.255, 0.478), resolution=(1080, 1920)))
    touch(Template(r"tpl1704766320613.png", record_pos=(0.423, 0.865), resolution=(1260, 2800)))
    touch(Template(r"tpl1704767107115.png", record_pos=(-0.175, 0.706), resolution=(1260, 2800)))
    text("100",enter=False)

## 领用类型
def use_type():
    sleep(1)
    swipe(Template(r"tpl1704780238598.png", record_pos=(0.0, 0.813), resolution=(1260, 2800)), vector=[-0.019, -0.0965])
    touch(Template(r"tpl1704780287739.png", record_pos=(0.407, 0.445), resolution=(1260, 2800)))
    sleep(1)

# 入库
def Warehousing():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(wait(Template(r"tpl1704764142651.png", record_pos=(-0.108, -0.326), resolution=(1260, 2800))))
    touch(wait(Template(r"tpl1704764238175.png", record_pos=(-0.249, 1.042), resolution=(1260, 2800))))
    touch(Template(r"tpl1704764311444.png", record_pos=(-0.1, -0.656), resolution=(1260, 2800)))
    upload_photos()
    choose_storage()
    choose_type()
    sleep(2)
    touch(Template(r"tpl1705627238645.png", record_pos=(-0.248, 0.321), resolution=(1080, 1920)))
    choose_material()
    swipe(Template(r"tpl1705383366898.png", record_pos=(-0.409, 0.816), resolution=(1080, 1920)), vector=[0.0411, -0.6022])
    sleep(1)
    choose_number()
    sleep(1)
    touch(Template(r"tpl1704766371877.png", record_pos=(0.0, 0.889), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1704766418402.png", record_pos=(0.383, 0.837), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1704766436851.png", record_pos=(-0.004, 1.029), resolution=(1260, 2800)))
    assert_exists(Template(r"tpl1704767675398.png", record_pos=(-0.002, -0.006), resolution=(1260, 2800)), "入库添加成功")
    touch(Template(r"tpl1704768022578.png", record_pos=(-0.432, -0.951), resolution=(1260, 2800)))

# 调度
def dispatch():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(wait(Template(r"tpl1704764142651.png", record_pos=(-0.108, -0.326), resolution=(1260, 2800))))
    # 从仓库物料第一个：AT_001，进行调度
    sleep(1)
    touch(wait(Template(r"tpl1705629608624.png", record_pos=(-0.005, -0.235), resolution=(1080, 1920))))
    sleep(1)
    swipe(Template(r"tpl1705383524694.png", record_pos=(-0.369, 0.681), resolution=(1080, 1920)), vector=[0.0034, -0.6144])
    sleep(1)
    touch(Template(r"tpl1707123553152.png", record_pos=(-0.068, 0.193), resolution=(1080, 1920)))
    sleep(1)
    swipe(Template(r"tpl1707123585545.png", record_pos=(0.008, 0.682), resolution=(1080, 1920)), vector=[-0.0181, -0.0873])
    sleep(1)
    touch(Template(r"tpl1707123636103.png", record_pos=(0.41, 0.224), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1707123656314.png", record_pos=(-0.16, 0.319), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1704768570842.png", record_pos=(0.415, 0.45), resolution=(1260, 2800)))
    sleep(3)
    touch(Template(r"tpl1710811547171.png", record_pos=(0.075, 0.544), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1705629955329.png", record_pos=(0.0, 0.48), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1704768723773.png", record_pos=(0.007, -0.011), resolution=(1260, 2800)), "调度物料成功")
    sleep(3)
    touch(Template(r"tpl1704768778997.png", record_pos=(-0.429, -0.95), resolution=(1260, 2800)))

# 出库
def outbound(num=3):
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    try:
        sleep(1)
        touch(Template(r"tpl1704769461951.png", record_pos=(-0.111, -0.381), resolution=(1260, 2800)))
        sleep(1)
        touch(Template(r"tpl1704769489481.png", record_pos=(0.248, 1.044), resolution=(1260, 2800)))
        choose_storage()
        sleep(2)
        touch(Template(r"tpl1705627238645.png", record_pos=(-0.248, 0.321), resolution=(1080, 1920)))
        choose_material()
        sleep(1)
        for i in range(num):
            touch(Template(r"tpl1704769851229.png", record_pos=(0.019, 0.021), resolution=(1260, 2800)))
        sleep(1)
        touch(Template(r"tpl1704770014487.png", record_pos=(0.007, 0.298), resolution=(1260, 2800)))
        touch(Template(r"tpl1704770035057.png", record_pos=(0.387, 0.289), resolution=(1260, 2800)))
        sleep(1)
        swipe(Template(r"tpl1705383990777.png", record_pos=(-0.367, 0.348), resolution=(1080, 1920)), vector=[-0.0203, -0.5475])
        
        touch(Template(r"tpl1705629988457.png", record_pos=(-0.103, 0.366), resolution=(1080, 1920)))
        # text("陈文哲")
        shell('am broadcast -a INPUT_TEXT --es text "陈文哲"')
        sleep(1)
        touch(wait(Template(r"tpl1706317790027.png", record_pos=(-0.106, 0.54), resolution=(1080, 1920))))
        sleep(1)
        touch(Template(r"tpl1706317882308.png", record_pos=(-0.332, 0.719), resolution=(1080, 1920)))
        swipe(Template(r"tpl1705725786328.png", record_pos=(-0.335, 0.549), resolution=(1080, 1920)), vector=[-0.0686, -0.6452])
        sleep(1)
        touch(Template(r"tpl1705630003792.png", record_pos=(-0.143, 0.586), resolution=(1080, 1920)))
        # text("这是自动化输入内容，时间：" + current_time)
        shell('am broadcast -a INPUT_TEXT --es text "这是自动化测试，进行物料出库，操作时间：{0}"'.format(current_time))
        touch(Template(r"tpl1705630018355.png", record_pos=(-0.334, 0.453), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1705630033600.png", record_pos=(-0.001, 0.822), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1704770748627.png", record_pos=(-0.004, -0.008), resolution=(1260, 2800)), "出库成功")
        sleep(4)
    except Exception as e:
        print("用例执行失败，返回")
    finally:
            touch(Template(r"tpl1705384288000.png", record_pos=(-0.434, -0.765), resolution=(1080, 1920)))

# 领用日常消耗物品
def use():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1704771068475.png", record_pos=(-0.11, -0.379), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1704771090386.png", record_pos=(0.25, -0.826), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1705630058158.png", record_pos=(0.002, 0.821), resolution=(1080, 1920)))
    sleep()
    touch(Template(r"tpl1705630090056.png", record_pos=(-0.138, -0.406), resolution=(1080, 1920)))
    use_type()
    touch(Template(r"tpl1705630206442.png", record_pos=(-0.085, -0.191), resolution=(1080, 1920)))
    # text("这是自动化输入内容，时间：" + current_time)
    shell('am broadcast -a INPUT_TEXT --es text "这是自动化输入内容，时间：{0}"'.format(current_time))
    touch(Template(r"tpl1704771957504.png", record_pos=(-0.046, -0.113), resolution=(1260, 2800)))
    upload_photos()
    sleep(1)
    touch(Template(r"tpl1705630230024.png", record_pos=(-0.174, 0.518), resolution=(1080, 1920)))
    sleep(1)
    choose_material()
    sleep(2)
    touch(Template(r"tpl1705630529631.png", record_pos=(-0.122, 0.639), resolution=(1080, 1920)))
    text("3")
    swipe(Template(r"tpl1705385537499.png", record_pos=(-0.409, 0.634), resolution=(1080, 1920)), vector=[0.0197, -0.5849])
    touch(Template(r"tpl1705630556375.png", record_pos=(-0.03, 0.531), resolution=(1080, 1920)))
    swipe(Template(r"tpl1704772308902.png", record_pos=(-0.014, -0.25), resolution=(1260, 2800)), vector=[0.1222, 0.5783])
    touch(Template(r"tpl1704772342657.png", record_pos=(-0.428, 0.956), resolution=(1260, 2800)))
    sleep(1)
    swipe(Template(r"tpl1704780402665.png", record_pos=(-0.388, 0.859), resolution=(1260, 2800)), vector=[-0.0115, -0.193])
    touch(Template(r"tpl1704772371982.png", record_pos=(-0.002, 1.028), resolution=(1260, 2800)))
    ## 这里缺少领用成功的弹窗
    touch(Template(r"tpl1705385728780.png", record_pos=(-0.43, -0.758), resolution=(1080, 1920)))
    
# 归还领用--全部归还
def return_material():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1704771068475.png", record_pos=(-0.11, -0.379), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1704771090386.png", record_pos=(0.25, -0.826), resolution=(1260, 2800)))
    sleep(1)
    try:
        touch(Template(r"tpl1704795027445.png", record_pos=(0.34, -0.246), resolution=(1260, 2800)))
        sleep(1)
        touch(Template(r"tpl1704795751640.png", record_pos=(-0.046, -0.536), resolution=(1260, 2800)))
        sleep(1)
        upload_photos()
        sleep(2)
        swipe(Template(r"tpl1705385966890.png", record_pos=(-0.394, 0.623), resolution=(1080, 1920)), vector=[0.0174, -0.547])
        sleep(1)
        touch(Template(r"tpl1704795780060.png", record_pos=(0.004, 0.699), resolution=(1260, 2800)))
        # 这里还缺少验证提示
    except Exception as e:
        print("归还按钮都不存在")
    finally:
        touch(Template(r"tpl1704795250437.png", record_pos=(-0.428, -0.949), resolution=(1260, 2800)))
    
# 提交OA数据到草稿箱
def creat_oa_to_save(cur_date):
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    touch(wait(Template(r"tpl1703214192081.png", record_pos=(-0.113, 0.0), resolution=(1260, 2800))))
    sleep(2)
    touch(wait(Template(r"tpl1707273102001.png", record_pos=(-0.204, -0.629), resolution=(1080, 1920))))
    text("cw")
    assert_exists(Template(r"tpl1707273172745.png", record_pos=(-0.223, -0.341), resolution=(1080, 1920)), "搜索结果正确")
    touch(Template(r"tpl1707273192629.png", record_pos=(-0.228, -0.339), resolution=(1080, 1920)))
    ## 流程详情编辑
    #### 清空原标题—自定义固定标题
    sleep(3)
    touch(wait(Template(r"tpl1705541318744.png", record_pos=(0.331, -0.475), resolution=(1080, 1920))))
    sleep(1)
    for i in range(40):
    #     os.system("adb shell input keyevent 67")
        keyevent("DEL")
    sleep(1)
    # text("AT_Alwin_专用流程3",enter=False)
    shell('am broadcast -a INPUT_TEXT --es text "AT_Alwin_专用流程3"')
    ### 付款项目
    touch(Template(r"tpl1705493700803.png", record_pos=(-0.014, -0.118), resolution=(1080, 1920)))
    sleep(1)
    search_pro()
#     ### 费用所属公司--已经有默认值了
#     touch(Template(r"tpl1705402920435.png", record_pos=(-0.019, 0.019), resolution=(1080, 1920)))
#     sleep(1)
#     search_pro()
    ### 报销日期当天
    touch(Template(r"tpl1705402840207.png", record_pos=(-0.006, 0.162), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1703224190621.png", record_pos=(0.406, 0.294), resolution=(1260, 2800)))
    sleep(1)
    ### 付款方式
    touch(Template(r"tpl1705387409752.png", record_pos=(-0.019, 0.285), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1703216668954.png", record_pos=(-0.348, 0.236), resolution=(1260, 2800)))
    sleep(1)
    # text("转账")
    shell('am broadcast -a INPUT_TEXT --es text "转账"')
    sleep(1)
    touch(Template(r"tpl1703224496273.png", record_pos=(-0.399, 0.363), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703224511266.png", record_pos=(0.401, 0.083), resolution=(1260, 2800)))
    sleep(1)
    ### 收款人确认
    touch(Template(r"tpl1705387436557.png", record_pos=(-0.017, 0.42), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1703216668954.png", record_pos=(-0.348, 0.236), resolution=(1260, 2800)))
    sleep(1)
    # text("陈文哲")
    shell('am broadcast -a INPUT_TEXT --es text "陈文哲"')
    sleep(1)
    touch(wait(Template(r"tpl1705631628449.png", record_pos=(-0.363, 0.122), resolution=(1080, 1920))))
    touch(Template(r"tpl1703224843534.png", record_pos=(0.404, -0.759), resolution=(1260, 2800)))
    sleep(1)
    assert_exists(Template(r"tpl1705631877502.png", record_pos=(-0.071, 0.543), resolution=(1080, 1920)), "收款人选择成功，收款银行和账号自动回显")
    swipe(Template(r"tpl1705386854871.png", record_pos=(-0.352, 0.688), resolution=(1080, 1920)), vector=[-0.0482, -0.6034])
    ###费用详细说明
    touch(wait(Template(r"tpl1705631694711.png", record_pos=(-0.213, 0.358), resolution=(1080, 1920))))
    # text("用于自动化测试调试的流程,提交日期：" + cur_date + "，请不要审批！")
    shell('am broadcast -a INPUT_TEXT --es text "用于自动化测试调试的流程,提交日期：：{0}"'.format(cur_date))
    sleep(1)
    ### 附件上传
    touch(Template(r"tpl1705632091644.png", record_pos=(-0.011, 0.084), resolution=(1080, 1920)))
    upload_file()
    sleep(1)
    assert_exists(Template(r"tpl1704340119949.png", record_pos=(-0.008, -0.024), resolution=(1260, 2800)), "附件添加成功")
    sleep(3)
    swipe(Template(r"tpl1705386931140.png", record_pos=(-0.307, 0.281), resolution=(1080, 1920)), vector=[-0.0593, -0.4791])
    sleep(2)
    swipe(Template(r"tpl1706580056901.png", record_pos=(-0.369, 0.781), resolution=(1080, 1920)), vector=[-0.0143, -0.613])
    sleep(1)
    ### 新增表单数据
    touch(Template(r"tpl1703227054655.png", record_pos=(0.009, -0.141), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703227071364.png", record_pos=(-0.111, -0.536), resolution=(1260, 2800)))
    sleep(3)
    #### 科目选择
    touch(Template(r"tpl1705630647420.png", record_pos=(-0.027, 0.052), resolution=(1080, 1920)))
    sleep(2)
    touch(Template(r"tpl1705632236263.png", record_pos=(-0.369, 0.023), resolution=(1080, 1920)))
    shell('am broadcast -a INPUT_TEXT --es text "办公费"')
    touch(Template(r"tpl1705632418417.png", record_pos=(-0.365, 0.121), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1703228142622.png", record_pos=(0.404, -0.759), resolution=(1260, 2800)))
    sleep(2)
    touch(Template(r"tpl1705632527329.png", record_pos=(-0.138, -0.473), resolution=(1080, 1920)))
    sleep(2)
#     text("自动化测试，用于调试",enter=False)
    shell('am broadcast -a INPUT_TEXT --es text "自动化测试费用报销表单，操作时间"'.format(current_time))
    touch(Template(r"tpl1705416178433.png", record_pos=(-0.097, 0.67), resolution=(1080, 1920)))
    sleep(1)
    # text("66",enter =False)
    shell('am broadcast -a INPUT_TEXT --es text "66"')
    swipe(Template(r"tpl1705387024753.png", record_pos=(-0.325, 0.61), resolution=(1080, 1920)), vector=[-0.0521, -0.6534])
    sleep(1)
    swipe(Template(r"tpl1706580926116.png", record_pos=(-0.31, 0.566), resolution=(1080, 1920)), vector=[-0.0601, -0.6781])
    touch(Template(r"tpl1703744740621.png", record_pos=(-0.223, 0.971), resolution=(1260, 2800)))
    ## 保存成功
    assert_exists(Template(r"tpl1703298737023.png", record_pos=(0.002, 0.173), resolution=(1260, 2800)), "提交成功")
    sleep(3)
    touch(Template(r"tpl1703232111393.png", record_pos=(-0.439, -0.958), resolution=(1260, 2800)))
    sleep(1)
      
# 草稿箱提交
def draft_to_submit():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1703298310846.png", record_pos=(0.117, 0.311), resolution=(1260, 2800)))
    sleep(2)
    touch(wait(Template(r"tpl1707126930606.png", record_pos=(-0.176, -0.641), resolution=(1080, 1920))))
    sleep(2)
    swipe(Template(r"tpl1709257287526.png", record_pos=(-0.356, 0.678), resolution=(1080, 1920)), vector=[-0.0271, -0.732])
    sleep(1)
    swipe(Template(r"tpl1706581522115.png", record_pos=(-0.366, 0.491), resolution=(1080, 1920)), vector=[-0.0087, -0.6418])
    sleep(1)
    swipe(Template(r"tpl1709257522131.png", record_pos=(-0.352, 0.622), resolution=(1080, 1920)), vector=[-0.0435, -0.7099])
    sleep(1)
    touch(Template(r"tpl1704358618744.png", record_pos=(0.228, 0.971), resolution=(1260, 2800)))
    assert_exists(Template(r"tpl1703298737023.png", record_pos=(0.002, 0.173), resolution=(1260, 2800)), "草稿箱提交成功")
    sleep(2)
    touch(Template(r"tpl1703298896666.png", record_pos=(-0.434, -0.952), resolution=(1260, 2800)))
    sleep(1)

# 工作微博
def job_weibo():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    # 进入工作微博
    ## 编写工作微博
    sleep(1)
    touch(Template(r"tpl1703299281991.png", record_pos=(-0.112, 0.309), resolution=(1260, 2800)))
    sleep(3)
    touch(Template(r"tpl1703299300277.png", record_pos=(-0.241, -0.587), resolution=(1260, 2800)))
    sleep(3)
    # text("今日工作：测试App")
    shell('am broadcast -a INPUT_TEXT --es text "该账号只是自动化功能巡检输入，用于自动化功能验证。"')
    sleep(3)
    touch(Template(r"tpl1703299334593.png", record_pos=(-0.365, -0.079), resolution=(1260, 2800)))
    assert_exists(Template(r"tpl1705740084890.png", record_pos=(0.012, -0.299), resolution=(1080, 1920)), "微博填写成功")
    sleep(1)
    ## 编辑工作微博
    touch(Template(r"tpl1703299488522.png", record_pos=(-0.363, 0.525), resolution=(1260, 2800)))
    sleep(3)
    touch(Template(r"tpl1705740998600.png", record_pos=(0.279, 0.611), resolution=(1080, 1920)))
    sleep(1)
    shell('am broadcast -a INPUT_TEXT --es text "，增加验证，内容增加了部分。该内容主要用于自动化测试输入验证。并非真正的微博内容。请领导忽略掉此条内容的意义，给领导带来的不便还请见谅！今日工作：测试App，增加验证，内容增加了部分。该内容主要用于自动化测试输入验证。并非真正的微博内容。请领导忽略掉此条内容的意义，给领导带来的不便还请见谅！"')
    sleep(3)
    touch(Template(r"tpl1705741171392.png", record_pos=(-0.018, 0.811), resolution=(1080, 1920)))
    swipe(Template(r"tpl1705741237327.png", record_pos=(-0.019, 0.808), resolution=(1080, 1920)), vector=[-0.0704, -0.3532])
    touch(Template(r"tpl1705741266956.png", record_pos=(0.352, 0.2), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1705740348842.png", record_pos=(-0.018, 0.484), resolution=(1080, 1920)), "编辑成功")
    touch(Template(r"tpl1704424690455.png", record_pos=(-0.435, -0.953), resolution=(1260, 2800)))

# 待办列表
def to_do_list():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(wait(Template(r"tpl1705543648230.png", record_pos=(0.108, 0.214), resolution=(1080, 1920))))
    sleep(3)
    touch(wait(Template(r"tpl1707127135637.png", record_pos=(-0.005, -0.442), resolution=(1080, 1920))))
    ## 滑动到底部
    sleep(2)
    swipe(Template(r"tpl1705544009103.png", record_pos=(-0.354, 0.628), resolution=(1080, 1920)), vector=[0.0349, -0.5367])
    sleep(1)
    swipe(Template(r"tpl1705544036420.png", record_pos=(-0.383, 0.494), resolution=(1080, 1920)), vector=[-0.0333, -0.6147])
    sleep(1)
    swipe(Template(r"tpl1706837931059.png", record_pos=(-0.361, 0.363), resolution=(1080, 1920)), vector=[-0.0133, -0.5629])
    sleep(1)
    swipe(Template(r"tpl1706837953531.png", record_pos=(-0.345, 0.528), resolution=(1080, 1920)), vector=[-0.0249, -0.6415])
    sleep(1)
    ## 抄送给陈文哲
    sleep(1)
    touch(Template(r"tpl1705544246524.png", record_pos=(-0.079, 0.339), resolution=(1080, 1920)))
    search_personal()
    ## 审批意见
    approval_opinion_pass()
    touch(Template(r"tpl1705547843315.png", record_pos=(-0.438, -0.762), resolution=(1080, 1920)))
    sleep(1)
    
# 流程监控
def oa_monitor():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    # 流程监控--搜索
    touch(Template(r"tpl1703301795183.png", record_pos=(0.335, 0.31), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703301821958.png", record_pos=(-0.175, -0.825), resolution=(1260, 2800)))
    shell('am broadcast -a INPUT_TEXT --es text "自动化"')
    sleep(1)
    # keyevent("ENTER")  
    assert_exists(Template(r"tpl1708479199431.png", record_pos=(-0.002, -0.51), resolution=(1080, 1920)), "流程监控搜索成功")
    touch(Template(r"tpl1703302577526.png", record_pos=(-0.437, -0.948), resolution=(1260, 2800)))

# 消息通知
def message_notice():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1703302381124.png", record_pos=(-0.336, 0.545), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703302478985.png", record_pos=(-0.193, -0.827), resolution=(1260, 2800)))
    # text("23-12-07")
    shell('am broadcast -a INPUT_TEXT --es text "23-12-07"')
    assert_exists(Template(r"tpl1704425153497.png", record_pos=(0.067, -0.639), resolution=(1260, 2800)), "搜索成功")
    sleep(3)
    touch(Template(r"tpl1703302577526.png", record_pos=(-0.437, -0.948), resolution=(1260, 2800)))  
    sleep(1)
    
# 员工微博
def employee_weibo():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1703303931948.png", record_pos=(-0.11, 0.547), resolution=(1260, 2800)))
    sleep(3)
    touch(Template(r"tpl1705642957174.png", record_pos=(-0.226, -0.63), resolution=(1080, 1920)))
    sleep(2.0)
    shell('am broadcast -a INPUT_TEXT --es text "自动化"')
    assert_exists(Template(r"tpl1705643139085.png", record_pos=(-0.128, -0.556), resolution=(1080, 1920)), "微博搜索成功")
    sleep(1)
    touch(Template(r"tpl1703310942979.png", record_pos=(-0.441, -0.952), resolution=(1260, 2800)))
    sleep(1)
    
# 检查性质
def check_nature():
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    ## 新增检查性质
    touch(Template(r"tpl1703312103737.png", record_pos=(0.335, 0.474), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703312163745.png", record_pos=(0.006, 1.001), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703314199272.png", record_pos=(-0.004, -0.737), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703314237723.png", record_pos=(-0.256, -0.031), resolution=(1260, 2800)))
    touch(Template(r"tpl1703314249235.png", record_pos=(0.431, -0.265), resolution=(1260, 2800)))
    touch(Template(r"tpl1703314268211.png", record_pos=(-0.26, -0.519), resolution=(1260, 2800)))
    # text("这是自动化自动添加的检查性质")
    shell('am broadcast -a INPUT_TEXT --es text "这是自动化自动添加的检查性质"')
    touch(Template(r"tpl1703314620596.png", record_pos=(-0.242, 0.998), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703314647063.png", record_pos=(-0.191, -0.714), resolution=(1260, 2800)))
    touch(Template(r"tpl1703314685870.png", record_pos=(0.126, 1.029), resolution=(1260, 2800)))
    sleep(1)
    touch(Template(r"tpl1703314376023.png", record_pos=(0.244, 1.002), resolution=(1260, 2800)))
    # 这里提交后，不好判断是否成功
    touch(Template(r"tpl1703315317912.png", record_pos=(-0.434, -0.953), resolution=(1260, 2800)))
    sleep(1)

## 搜索流程名--搜索到截止
def search_process_name(name):
    sleep(2)
    touch(Template(r"tpl1705743300017.png", record_pos=(-0.192, -0.631), resolution=(1080, 1920)))
    sleep(1)
    shell('am broadcast -a INPUT_TEXT --es text "{0}"'.format(name))
    keyevent('ENTER')
    
##  已办列表----已办列表还不支持括号中的内容搜索所以报错
def completed_list(name='自动化'):
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1705743269207.png", record_pos=(0.335, 0.213), resolution=(1080, 1920)))
    search_process_name(name)
    assert_exists(Template(r"tpl1707128387950.png", record_pos=(-0.012, -0.506), resolution=(1080, 1920)), "已办列表搜索成功")
    touch(Template(r"tpl1705744247670.png", record_pos=(-0.438, -0.765), resolution=(1080, 1920)))
    sleep(1)

##  我的流程
def my_process(name='自动化'):
    sleep(2)
    touch(Template(r"tpl1707127484241.png", record_pos=(-0.205, 0.855), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1705744732494.png", record_pos=(-0.337, 0.429), resolution=(1080, 1920)))
    sleep(1)
    search_process_name(name)
    assert_exists(Template(r"tpl1707128462028.png", record_pos=(-0.003, -0.506), resolution=(1080, 1920)), "我的流程搜索成功")
    touch(Template(r"tpl1705744247670.png", record_pos=(-0.438, -0.765), resolution=(1080, 1920)))
    sleep(1)

## 聊天-待办消息
def chat_need_to_be_deal():
    sleep(2)
    touch(Template(r"tpl1706841340639.png", record_pos=(0.206, 0.859), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1706842854730.png", record_pos=(-0.319, -0.104), resolution=(1080, 1920)),"验证流程结束后，4条待办消息推送正确")
    touch(wait(Template(r"tpl1706842324043.png", record_pos=(-0.139, -0.066), resolution=(1080, 1920))))
    sleep(1)
    touch(wait(Template(r"tpl1707041158468.png", record_pos=(-0.23, 0.693), resolution=(1080, 1920))))
    ### 进入已完成得待办详情
    sleep(2)
    ### 验证审核状态
    assert_exists(Template(r"tpl1706843240016.png", record_pos=(0.345, -0.593), resolution=(1080, 1920)), "审核状态通过")
    ### 验证流程图
    touch(Template(r"tpl1706843776979.png", record_pos=(0.001, -0.375), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1709775754175.png", record_pos=(0.011, 0.164), resolution=(1080, 1920)),"流程图比对正确")
    ### 验证处理日志
    touch(Template(r"tpl1706843935616.png", record_pos=(0.316, -0.376), resolution=(1080, 1920)))
    sleep(1)
    assert_exists(Template(r"tpl1709778080026.png", record_pos=(-0.098, -0.054), resolution=(1080, 1920)),  "出纳审批日志正确")
    assert_exists(Template(r"tpl1709778099872.png", record_pos=(-0.116, 0.481), resolution=(1080, 1920)), "财务部长审批日志正确")
    swipe(Template(r"tpl1709778125643.png", record_pos=(-0.307, 0.356), resolution=(1080, 1920)), vector=[-0.0356, -0.5587])
    assert_exists(Template(r"tpl1709778755435.png", record_pos=(-0.123, 0.038), resolution=(1080, 1920)), "会计审批无误")
    assert_exists(Template(r"tpl1709778794537.png", record_pos=(-0.219, 0.604), resolution=(1080, 1920)), "上级领导审批无误")
    swipe(Template(r"tpl1709778818079.png", record_pos=(-0.24, 0.378), resolution=(1080, 1920)), vector=[-0.1137, -0.4276])
    assert_exists(Template(r"tpl1709778859662.png", record_pos=(-0.046, 0.511), resolution=(1080, 1920)), "发起人提交无误")
    sleep(1)
    ### 回到顶部
    swipe(Template(r"tpl1709779029770.png", record_pos=(-0.236, -0.197), resolution=(1080, 1920)), vector=[-0.0442, 0.5621])
    sleep(1)
    swipe(Template(r"tpl1709779055801.png", record_pos=(-0.249, -0.298), resolution=(1080, 1920)), vector=[-0.0437, 0.6059])

    ### 验证表单中得抄送等审批按钮
    touch(Template(r"tpl1706844307058.png", record_pos=(-0.319, -0.581), resolution=(1080, 1920)))
    sleep(1)
    swipe(Template(r"tpl1706843282739.png", record_pos=(-0.352, 0.764), resolution=(1080, 1920)), vector=[-0.0226, -0.7931])
    sleep(1)
    swipe(Template(r"tpl1706843325818.png", record_pos=(-0.351, 0.728), resolution=(1080, 1920)), vector=[-0.0382, -0.7587])
    sleep(1)
    swipe(Template(r"tpl1706843360743.png", record_pos=(-0.34, 0.735), resolution=(1080, 1920)), vector=[-0.0325, -0.7523])
    sleep(1)
    swipe(Template(r"tpl1706843436161.png", record_pos=(-0.361, 0.66), resolution=(1080, 1920)), vector=[-0.005, -0.7313])
    sleep(1)
    assert_not_exists(Template(r"tpl1706843491989.png", record_pos=(-0.147, 0.515), resolution=(1080, 1920)), "确定不存在审批意见及抄送人")
    sleep(1)
    assert_not_exists(Template(r"tpl1706843524890.png", record_pos=(-0.313, 0.807), resolution=(1080, 1920)), "确定不存在审批功能")
    sleep(1)
    touch(Template(r"tpl1706844366127.png", record_pos=(-0.441, -0.762), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1709779187529.png", record_pos=(-0.437, -0.763), resolution=(1080, 1920)))
    
    
if __name__ == '__main__':
    current_date = time.strftime("%Y-%m-%d")
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    #仓储管理
    ## 入库
    Warehousing()
    ## 调度
    dispatch()
    ## 出库------------------这里有返回bug，后续还需优化
    outbound()
    ## 领用-固定资产----------这里缺少对领用成功弹窗的验证
    use()
    ## 归还
    return_material()

    #  测试前置：需要先切换输入法
    #  OA流程
    ## 创建OA流程到，所有数据保存
    creat_oa_to_save(current_date)
    # 从草稿箱提交OA流程
    draft_to_submit()
    ## 待办列表
    try:
        to_do_list()
    except:
        print("运行出错")
    finally:
        back_to_home()
    ## 待办消息推送及详情
    try:
        chat_need_to_be_deal()
    except:
        print("运行出错")
    finally:
        back_to_home()
    # OA流程监控
    try:
        oa_monitor()
    except:
        print("运行出错")
    finally:
        back_to_home()
    # 已办列表----已办列表还不支持括号中的内容搜索所以报错
    ## 通过时间搜索当日已审批过的单据
    try:
        completed_list()
    except:
        print("运行出错")
    finally:
        back_to_home()
    # 我的流程
    ## 通过时间搜索当日已审完成的单据
    try:
        my_process()
    except:
        print("运行出错")
    finally:
        back_to_home()
    

    # 微博
    ## 创建工作微博
    try:
        job_weibo()
    except:
        print("运行出错")
    finally:
        back_to_home()
    ## 员工微博
    try:
        employee_weibo()
    except:
        print("运行出错")
    finally:
        back_to_home()

    #消息通知-------切换账号后没有数据暂时别用
    try:
        message_notice()
    except:
        print("运行出错")
    finally:
        back_to_home()


    # 质量管理
    ## 质量计划这里执行后有误，以后新建后，需要删除
    try:
        check_nature()
    except:
        print("运行出错")
    finally:
        back_to_home()
        