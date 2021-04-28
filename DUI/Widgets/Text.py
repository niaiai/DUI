#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: *.py
from DUI.enums import WidgetEnum, TextAlignEnum
from DUI.Widgets import Widget
from DUI.bin import *


class Text(Widget):
    def __init__(self, text="", pointed_text="", text_align: TextAlignEnum = TextAlignEnum.LEFT, widget_id=None):
        super().__init__(WidgetEnum.TEXT, widget_id)
        self.text = text
        # 0 左对齐 1 居中 2 右对齐
        self.text_align = text_align
        self.pointed_text = pointed_text

    def render(self, width, system, checked=None, **kwargs):
        # 根据系统调整空格大小(此版本无效)
        long = width
        b = 2
        if checked:
            text = self.pointed_text + self.text
        else:
            text = " " * len(self.pointed_text) + self.text
        textLength = slen(text)

        if self.text_align is TextAlignEnum.LEFT:
            '''左对齐'''
            return text + " " * (long - textLength - b)
        if self.text_align is TextAlignEnum.CENTER:
            '''居中'''
            a = int((long - textLength - b) / 2)
            return " " * a + text + " " * (long - a - textLength - 2)
        else:
            '''右对齐'''
            return " " * (long - textLength - 2) + text
