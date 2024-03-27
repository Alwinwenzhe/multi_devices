# -*- encoding=utf8 -*-
__author__ = "EDY"
from airtest.core.api import *
auto_setup(__file__)


def init_dev():
    '''
    有了它，每次运行前，就会自动连接虚拟机，不用先链接设备再测试了
    '''
    dev = connect_device("android://127.0.0.1:5037/127.0.0.1:16384?cap_method=ADBCAP&touch_method=MAXTOUCH&")
    auto_setup(__file__)

def search_chat():
    touch(wait(Template(r"tpl1711422517214.png", record_pos=(0.338, -0.764), resolution=(1080, 1920))))
    sleep(2)
    touch(Template(r"tpl1711453450611.png", record_pos=(-0.299, -0.764), resolution=(1080, 1920)))
    sleep(2)
    shell('am broadcast -a INPUT_TEXT --es text "测试组"')
    touch(wait(Template(r"tpl1711338257421.png", record_pos=(0.35, -0.761), resolution=(1080, 1920))))
    sleep(1)
    assert_exists(Template(r"tpl1711354478720.png", record_pos=(-0.317, -0.089), resolution=(1080, 1920)), "群聊搜索成功")
    
def send_text(cur_time,i):
    '''
    发送文字
    '''
    touch(wait(Template(r"tpl1711338808158.png", record_pos=(0.003, 0.829), resolution=(1080, 1920))))
    shell('am broadcast -a INPUT_TEXT --es text "现在的时间是：{0}，这是第{1}次输入！"'.format(cur_time,i))
    sleep(1)
    touch(Template(r"tpl1711346048376.png", record_pos=(0.401, 0.787), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1711346896447.png", record_pos=(-0.094, 0.413), resolution=(1080, 1920)), "消息发送成功")
    
def send_text2():
    '''
    发送固定文字
    '''
    touch(wait(Template(r"tpl1711338808158.png", record_pos=(0.003, 0.829), resolution=(1080, 1920))))
    shell('am broadcast -a INPUT_TEXT --es text "2017年，熊猫不走于惠州成立，其最大的特色，是在送蛋糕上门的同时，配送员还会身穿熊猫玩偶服带来一段表演助兴，这也是“熊猫不走”名字的由来。可能很多人发现了，熊猫不走的这一套和海底捞有点像，都是主打服务，庆生的时候给顾客来一段表演，通过这种别出心裁的方式来增加仪式感。！"')
    sleep(1)
    touch(Template(r"tpl1711346048376.png", record_pos=(0.401, 0.787), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1711346896447.png", record_pos=(-0.094, 0.413), resolution=(1080, 1920)), "消息发送成功")    
    
def transmit_message():
    send_text2()
    touch(wait(Template(r"tpl1711434299137.png", record_pos=(0.03, 0.317), resolution=(1080, 1920))),duration=2)
    touch(wait(Template(r"tpl1711435613967.png", record_pos=(-0.145, 0.749), resolution=(1080, 1920))))
    sleep(2)
    touch(wait(Template(r"tpl1711435651944.png", record_pos=(-0.322, -0.529), resolution=(1080, 1920))))
    touch(Template(r"tpl1711435672704.png", record_pos=(0.164, 0.152), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1711435822522.png", record_pos=(0.006, -0.764), resolution=(1080, 1920)), "转发成功")
    
def quote_reply():
    '''
    引用回复
    '''
    send_text2()
    touch(wait(Template(r"tpl1711434299137.png", record_pos=(0.03, 0.317), resolution=(1080, 1920))),duration=2)
    touch(wait(Template(r"tpl1711434324964.png", record_pos=(0.004, -0.231), resolution=(1080, 1920))))
    touch(wait(Template(r"tpl1711434402586.png", record_pos=(-0.048, 0.832), resolution=(1080, 1920))))
    shell('am broadcast -a INPUT_TEXT --es text "可惜还是跑路了额！"')
    touch(wait(Template(r"tpl1711434475923.png", record_pos=(0.359, 0.821), resolution=(1080, 1920))))
    assert_exists(Template(r"tpl1711434501950.png", record_pos=(0.004, 0.671), resolution=(1080, 1920)), "引用成功")

def withdraw_message():
    '''
    撤回消息
    '''
    send_text2()
    touch(Template(r"tpl1711435931648.png", record_pos=(0.013, 0.022), resolution=(1080, 1920)),duration=2)
    touch(wait(Template(r"tpl1711435284874.png", record_pos=(0.145, -0.227), resolution=(1080, 1920))))
    touch(wait(Template(r"tpl1711435341766.png", record_pos=(0.126, 0.142), resolution=(1080, 1920))))
    assert_exists(Template(r"tpl1711435358935.png", record_pos=(-0.006, 0.718), resolution=(1080, 1920)), "撤回成功")

def send_expression():
    '''
    发送表情--
    '''
    sleep(1)
    touch(wait(Template(r"tpl1711423753465.png", record_pos=(0.349, 0.831), resolution=(1080, 1920))))
    touch(wait(Template(r"tpl1711346512508.png", record_pos=(-0.404, 0.086), resolution=(1080, 1920))))
    touch(wait(Template(r"tpl1711346549264.png", record_pos=(0.402, -0.064), resolution=(1080, 1920))))
    sleep(1)
    assert_exists(Template(r"tpl1711346940221.png", record_pos=(0.266, 0.686), resolution=(1080, 1920)), "表情发送成功")
    
def send_photo():
    '''
    发送图片
    '''
    touch(wait(Template(r"tpl1711351040783.png", record_pos=(0.443, 0.829), resolution=(1080, 1920))))
    touch(wait(Template(r"tpl1711353500805.png", record_pos=(-0.384, 0.144), resolution=(1080, 1920))))
    touch(wait(Template(r"tpl1711353532683.png", record_pos=(0.006, -0.185), resolution=(1080, 1920))))
    touch(Template(r"tpl1711353550760.png", record_pos=(0.373, -0.757), resolution=(1080, 1920)))
    assert_exists(Template(r"tpl1711353583190.png", record_pos=(0.087, -0.288), resolution=(1080, 1920)), "发送图片成功")

def send_vedio():
    '''
    发送视频
    '''
    # touch(wait(Template(r"tpl1711351040783.png", record_pos=(0.443, 0.829), resolution=(1080, 1920))))   
    # 这里因为上一个用例发送图片后，没有自动收缩，这里不要点击
    touch(wait(Template(r"tpl1711356048364.png", record_pos=(0.387, 0.233), resolution=(1080, 1920))))
    sleep(1)
    touch(Template(r"tpl1711356065604.png", record_pos=(-0.001, 0.651), resolution=(1080, 1920)))
    sleep(3)
    touch(wait(Template(r"tpl1711424006595.png", record_pos=(-0.333, -0.555), resolution=(1080, 1920))))
    touch(Template(r"tpl1711362487391.png", record_pos=(0.374, -0.758), resolution=(1080, 1920)))
    sleep(6)
    assert_exists(Template(r"tpl1711432096087.png", record_pos=(0.05, 0.458), resolution=(1080, 1920)), "发送视频成功")
    # 这里因为上一个用例发送图片后，没有自动收缩，这里得多点击一次
    touch(wait(Template(r"tpl1711351040783.png", record_pos=(0.443, 0.829), resolution=(1080, 1920))))   

    
if __name__ == '__main__':
    current_date = time.strftime("%Y-%m-%d")
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    init_dev()
    touch(wait(Template(r"tpl1711338947502.png", record_pos=(0.204, 0.816), resolution=(1080, 1920))))
    search_chat()
    touch(wait(Template(r"tpl1711354378471.png", record_pos=(-0.333, -0.093), resolution=(1080, 1920))))
    for i in range(2):
        send_text(current_date,i)
        quote_reply()
        withdraw_message()
        transmit_message()
        # 注意这里转发后，错误的回到了聊天列表，所以需要
        touch(wait(Template(r"tpl1711354378471.png", record_pos=(-0.333, -0.093), resolution=(1080, 1920))))
        send_expression()
        send_photo()
        send_vedio()
        
         


