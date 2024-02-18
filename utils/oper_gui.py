import pyautogui,time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False


class GuiFunction(object):

    def double_click_pic(self,pic_name=r'pic/mumu_start.png'):
        pyautogui.hotkey('win', 'd')
        coords = pyautogui.locateOnScreen(pic_name,confidence=0.9)
        if coords is not None:
            print('找到了，进行双击运行')
            x,y = pyautogui.center(coords)
            pyautogui.doubleClick(x,y)
        else:
            print('没找到:'+ pic_name)

    def left_click_pic(self,pic_name=r'pic/mumu_jnt.png'):
        coords = pyautogui.locateOnScreen(pic_name,confidence=0.9)
        if coords is not None:
            print('找到了，左键单击')
            x, y = pyautogui.center(coords)
            pyautogui.leftClick(x, y)
        else:
            print('没找到:'+ pic_name)
        time.sleep(6)

    def cmd_connect_mumu(self,pic_name=r'pic/cmd_enter.png'):
        pyautogui.hotkey('win', 'r')
        coords = pyautogui.locateOnScreen(pic_name, confidence=0.8)
        if coords is not None:
            print('找到了，进行双击运行')
            x, y = pyautogui.center(coords)
            pyautogui.leftClick(x, y)
        else:
            print('没找到:'+ pic_name)
        pyautogui.typewrite('adb  connect  127.0.0.1:16448', 1)  # 输入文本
        time.sleep(2)
        pyautogui.typewrite(['enter'])  # 调用enter键
        time.sleep(3)
        pyautogui.hotkey("alt","F4")
        self.left_click_pic(r'pic/mumu_title.png')


if __name__ == '__main__':
    pass
    # gui = GuiFunction()
    # # gui.cmd_connect_mumu()
