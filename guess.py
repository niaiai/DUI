#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: guess.py

"""
DUI使用案例: 猜数游戏
    游戏将从0到10随机抽取一个数字, 用户输入数字, 系统会提示是否正确
    游戏有3个界面：主界面、游戏界面、结束界面
DUI控件使用:
    Frame
    Window * 3
    Listener
    Text
    Button
"""

from DUI import *
from random import randint

from DUI.enums import TextAlignEnum


def mainW():
    frame.showWindow(0)


def guess():
    an = randint(0, 2)
    frame.showWindow(1)
    while True:
        txt = listen.getText()
        try:
            res = int(txt)
        except:
            continue
        if res == an:
            # 猜对
            gameWindow.updateWidget(0, Alert())
            frame.addWindow(gameWindow, 1)
            frame.showWindow(2)
            frame.listener.run()
            return
        else:
            # 猜错
            gameWindow.updateWidget(0, Alert("猜错了！不是" + str(res)))
            frame.addWindow(gameWindow, 1)
            frame.showWindow(1)


frame = Frame()

# 主界面
mainWindow = Window("主界面")
mainWindow.addWidget(2, Text("猜数游戏", text_align=TextAlignEnum.CENTER))
mainWindow.addWidget(5, Button("开始游戏", on_click=guess))
mainWindow.addWidget(6, Button("结束游戏", on_click=quit))
frame.addWindow(mainWindow, 0)

# 游戏界面
gameWindow = Window("猜数界面")
gameWindow.addWidget(0, Alert())
gameWindow.addWidget(2, Text("猜猜随机出来的是几(0-10)"))
gameWindow.addWidget(4, Text())
frame.addWindow(gameWindow, 1)

# 游戏结束界面
overWindow = Window("猜数成功!")
overWindow.addWidget(2, Text("恭喜你猜对了！", text_align=TextAlignEnum.CENTER))
overWindow.addWidget(5, Button("返回主界面", on_click=mainW))  # 此处不设置onClick事件来跳入while主循环
frame.addWindow(overWindow, 2)

# 设置监听器
listen = Listener(mode=0)
keys = {
    "quit": quit,
    "exit": quit,
    "w": mainWindow.up,
    "s": mainWindow.down,
    "y": listen.confirm,
    "\n": None
}
listen.dict = keys

frame.setListener(listen)

if __name__ == "__main__":
    # 主程序开始
    while True:
        frame.showWindow(0)
        frame.listener.run()
