#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: Frame.py

from DUI.Frames.Listener import *
from DUI.bin import clear
import time


class Frame:
    def __init__(self, showFPS=False, noClean=False):
        self.windows = []  # 储存window
        self.alert = None
        self.listener = Listener(0)
        self.nowWindow = None
        self.showFPS = showFPS
        self.noClean = noClean
        # clear
        clear()

    '''
        设置窗口皮肤
    '''
    def setSkin(self, skinList):
        self.skin = skinList

    '''
        传入一个自定义的Listener
    '''
    def setListener(self, listener):
        self.listener = listener

    '''
        添加新的窗口
    '''
    def addWindow(self, window, index):
        try:
            self.windows[index] = window
        except:
            self.windows.append(window)

    def updateWindow(self, window, index):
        self.windows[index] = window

    def delWindow(self, index):
        del self.windows[index]

    '''
        调用窗口的显示方法来切换窗口
    '''
    def showWindow(self, index):
        if self.showFPS:
            time_start = time.time()  # 开始计时

        win = self.windows[index]
        win.showWindow(noClean=self.noClean)
        self.nowWindow = index
        pointButton = win.getPointButton()
        if pointButton != None:
            self.listener.setPointButton(pointButton)

        if self.showFPS:
            time_use = time.time() - time_start  # 计时
            if time_use == 0:
                FPS = "   +∞"
            else:
                FPS = "% 5d" % int(1 / time_use)
            print("FPS:", FPS)
