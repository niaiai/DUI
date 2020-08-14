#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: Button.py

from DUI.Widgets import Text
from DUI.bin import *

class Button(Text):
	def __init__(self, text="", mode=False, id=None):
		super().__init__(text, id=id)
		self.isPointed = mode
		super(Text, self).setType("Button")

	def pointed(self):
		self.isPointed = True
	def leave(self):
		self.isPointed = False

	def press(self, func):
		func()

	'''
		绘制按钮  mode: 0 未选中 1 选中
	'''
	def print(self, width, system, mode=0):
		text = super().getText()
		if self.isPointed:
			super().setText(">|" + text)
			temp = super().print(width, system)
			super().setText(text)
			return temp
		return super().print(width, system)
# def getText(self, width, system):
	# 	if system == 0:
	# 		long = width
	# 		b = 2
	# 		textLength = slen(self.text)
	# 	else:
	# 		long = width
	# 		textLength = slen(self.text)
	# 		b = 0
	#
	# 	# if self.ispointed:
	# 	# 	color = "\033[32;40m"
	# 	# else:
	# 	# 	color = "\033[37;40m"
	#
	# 	'''居中'''
	# 	a = int((long - textLength - b) / 2)
	# 	# return " " * a + color +self.text + "\033[0m" + " " * (long - a - textLength - 2)
	# 	return " " * a + self.text +  " " * (long - a - textLength - 2)
