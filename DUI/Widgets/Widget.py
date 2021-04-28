#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: Widget.py
from DUI.enums import WidgetEnum


class Widget:
    def __init__(self, widget_type: WidgetEnum, widget_id=None):
        # 标注控件类型
        self.widget_type = widget_type
        self.widget_id = widget_id

    def render(self, *args, **kwargs):
        pass
