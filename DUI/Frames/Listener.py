#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: Listener.py

from DUI.Widgets import Widget
from DUI.enums import WidgetEnum


class Listener(Widget):
    def __init__(self, keys=None, mode=0):
        super().__init__(WidgetEnum.LISTENER)  # 参数: 标明自身类型
        self.mode = mode  # 0 为原生input监听   1 为C扩展监听

        if keys is None:
            keys = {
                "w": print("up"),
                "s": print("down"),
                "a": print("left"),
                "d": print("right"),
                "\n": None
            }
        self.dict = keys
        self.pointButton = None


    def setPointButton(self, button):
        self.pointButton = button[1]

    def getText(self):
        return input("->")

    def run(self):
        if self.mode == 0:
            res = input("->")  # 按键结果
            for key, func in self.dict.items():
                if res == "\n":
                    return False
                if res == key:
                    func()
        return True

    # 按钮确认键
    def confirm(self):
        self.pointButton.press()
