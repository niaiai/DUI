#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: Button.py

from DUI.enums import WidgetEnum, TextAlignEnum
from DUI.Widgets import Text


class Button(Text):
    def __init__(self, text="",
                 pointed_text=">|",
                 text_align: TextAlignEnum = TextAlignEnum.LEFT,
                 is_pointed=False,
                 widget_id=None,
                 on_click=None):
        super().__init__(text, pointed_text, text_align=text_align, widget_id=widget_id)
        self.widget_type = WidgetEnum.BUTTON
        self.is_pointed = is_pointed  # 指针是否指向当前Button bool (False 未选中 True 选中)
        self.on_click = on_click  # 点击事件

    def pointed(self):
        self.is_pointed = True

    def leave(self):
        self.is_pointed = False

    def press(self):
        self.on_click()

    def render(self, width, system):
        return super().render(width, system, self.is_pointed)
