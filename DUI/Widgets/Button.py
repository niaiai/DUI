#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: Button.py

from DUI.Widgets import Text


class Button(Text):
    def __init__(self, text="", checked_prefix_text=">|", mode=False, id=None, onClick=None):
        super().__init__(text, checked_prefix_text, id=id)
        super().setType("Button")
        self.isPointed = mode  # 指针是否指向当前Button bools
        self.onClick = onClick  # 点击事件

    def pointed(self):
        self.isPointed = True

    def leave(self):
        self.isPointed = False

    def setOnClick(self, func):
        self.onClick = func

    def press(self):
        self.onClick()

    '''
        绘制按钮  mode: 0 未选中 1 选中
    '''
    def print(self, width, system, mode=0):
        return super().print(width, system, self.isPointed)
