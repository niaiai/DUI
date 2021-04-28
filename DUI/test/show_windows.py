import time
from DUI import *
from DUI import __version__
from DUI.enums import TextAlignEnum


def test1():
    print("测试按钮1被点击")
    time.sleep(1)


def test2():
    print("测试按钮2被点击")
    time.sleep(1)


def test3():
    print("测试按钮3被点击")
    time.sleep(1)


def showTestWindow():
    f = Frame()

    mainWindow = Window("主界面")
    mainWindow.addWidget(2, Text("DUI库的测试窗口", text_align=TextAlignEnum.LEFT))
    mainWindow.addWidget(4, Text("版本:" + __version__(), text_align=TextAlignEnum.CENTER))
    mainWindow.addWidget(6, Text("作者:Lettle", text_align=TextAlignEnum.CENTER))
    mainWindow.addWidget(8, Text("w向上s向下y确认", text_align=TextAlignEnum.CENTER))
    mainWindow.addWidget(9, Text("一起学习?加作者QQ:1071445082", text_align=TextAlignEnum.CENTER))
    mainWindow.addWidget(10, Text("---By Lettle", text_align=TextAlignEnum.RIGHT))
    mainWindow.addWidget(11, Button("测试按钮1", on_click=test1))
    mainWindow.addWidget(12, Button("测试按钮2", on_click=test2))
    mainWindow.addWidget(13, Button("测试按钮3", on_click=test3))
    mainWindow.addWidget(14, Button("退出(点击或输入quit)", on_click=quit))
    f.addWindow(mainWindow, 0)

    keys = {
        "quit": quit,
        "w": mainWindow.up,
        "s": mainWindow.down,
        "y": mainWindow.confirm
    }
    listen = Listener(keys, 0)
    f.setListener(listen)

    while True:
        f.showWindow(0)
        f.listener.run()


if __name__ == "__main__":
    showTestWindow()
