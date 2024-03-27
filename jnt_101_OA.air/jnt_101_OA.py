# -*- encoding=utf8 -*-
__author__ = "EDY"

from airtest.core.api import *
auto_setup(__file__)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #引入键盘
from airtest_selenium.proxy import WebChrome

from selenium.webdriver.firefox.options import Options

# 1. 初始化配置对象
options = Options()
# 2. 无界面模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# 3. 添加请求头伪装浏览器
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0')
# 4. 告诉浏览器去掉了webdriver痕迹
options.add_argument("--disable-blink-features=AutomationControlled")
# 5. 不加载图片提高访问速度
options.add_argument('blink-settings=imagesEnabled=false')
options.add_argument('--disable-images')
driver = webdriver.Firefox(options=options)
# 6. 隐式等待10秒
driver.implicitly_wait(10)
# 设置进入的网址
driver.get("http://47.109.89.50:3000/#/login")

sleep(10)
driver.quit()
