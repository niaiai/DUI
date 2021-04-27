#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: *.py
from DUI.Widgets import Widget
from DUI.bin import *

class Text(Widget):
	def __init__(self, text="", checked_prefix_text="", type=0, id=None):
		super().__init__("Text", id)
		self.text = text
		# 0 左对齐 1 居中 2 右对齐
		self.type = type
		self.checked_prefix_text = checked_prefix_text
		# self.setText(text,type)


	def setText(self, text, type=0):
		self.text = text
		self.type = type
	def getText(self):
		return self.text

	def getType(self):
		return super().getType()
	def setType(self, type):
		super().setType(type)

	def print(self, width, system, checked=None):
		# 根据系统调整空格大小(此版本无效)
		# if system == 0:
		# 	long = width
		# 	b = 2
		# 	textLength = slen(self.text)
		# else:
		# 	long = width
		# 	textLength = slen(self.text)
		# 	b = 0

		long = width
		b = 2
		if checked:
			text = self.checked_prefix_text + self.text
		else:
			text = " " * len(self.checked_prefix_text) + self.text
		textLength = slen(text)

		if self.type == 0:
			'''左对齐'''
			return text + " " * (long - textLength - b)
		elif self.type == 1:
			'''居中'''
			a = int((long - textLength - b) / 2)
			return " " * a + text + " " * (long - a - textLength - 2)
		else:
			'''右对齐'''
			return " " * (long - textLength - 2) + text
