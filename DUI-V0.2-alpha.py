#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#python3
__author__='Lettle'
import os,sys,re
from ctypes import *
#基础方法
def slen(value):
    length =len(value)
    utf8_length =len(value.encode('utf-8'))
    length =(utf8_length -length)/2+length
    return int(length)
#控件库-----------------------------------------------------------
class Window():
    def __init__(self,title,mark):
        self.mark = mark
        self.title = title
        self.sys = "Linux"
        self.height = 20
        self.width = 40
        self.widget = []
    def set_sys(self,sys):
        self.sys = sys
    def set_size(self,height,width):
        self.height = int(height)
        self.width = int(width)
    def add_widget(self,widget_name,widget_location,way='L',text='widget',cursor_index=0):
        for i in range(1):        #更新控件库记得修改这里---------
            if widget_name == "line" or widget_name == 'Line':
                widget = Line(widget_location-1)
            elif widget_name == 'TextLine':
                widget = TextLine(text,way,widget_location-1)
            elif widget_name == 'Button':
                widget = Button(text,way,widget_location-1,cursor_index=cursor_index)
        self.widget.append(widget)
    def buildW(self,Frame):
        if self.sys == "Windows":  #判断系统进行清屏
            os.system("cls")
        else:
            os.system("clear")
        def build_fbte(i):        #fbte:From begining to end
            if i == 0:
                print("╔"+"═"*2+self.title+"═"*(self.width-7-slen(self.title))+'-'+'□'+'x'+"╗")
                return False
            elif i == self.height-1:
                print("╚"+"═"*(self.width-2)+"╝")
                return False
            else:
                return True

        def refresh_button():
            for i in range(len(widget_task)):
                if widget_task[i].mark == 3:
                    if Frame.cursor == widget_task[i].cursor_index:
                        widget_task[i].select=True
                    else:
                        widget_task[i].select=False
        widget_a = len(self.widget)
        if widget_a == 0:        #判断有无控件
            for i in range(self.height):
                if build_fbte(i):
                    print("║"+" "*(self.width-2)+"║")
        else:
            widget_task = self.widget
            a = 0 #控制下面空白区域的显示
            Button_num = 0
            refresh_button()
            for i in range(self.height):
                if build_fbte(i):
                    if widget_a != 0:
                        for ii in range(widget_a):
                            if widget_task[ii].location == i:    #查询当前控件任务的位置
                                if widget_task[ii].mark == 0:    #分隔条
                                    print("╠"+"═"*(self.width-2)+"╣")
                                elif widget_task[ii].mark == 1:  #文本条
                                    if slen(widget_task[ii].text)>(self.width-2):
                                        text = re.findall(r'.{'+str(self.width-2)+r'}',widget_task[ii].text)
                                        print("║"+text[0]+"║")
                                    elif widget_task[ii].way == 'L':
                                        print("║"+widget_task[ii].text+' '*(self.width-2-slen(widget_task[ii].text))+"║")
                                    elif widget_task[ii].way == 'C':
                                        iii = int((self.width-2-slen(widget_task[ii].text))/2)
                                        inte = slen(widget_task[ii].text)
                                        print("║"+' '*iii+widget_task[ii].text+' '*(self.width-2-iii-inte)+"║")
                                    elif widget_task[ii].way == 'R':
                                        print("║"+(r'{:>'+str(self.width-2)+r'}').format(widget_task[ii].text)+"║")
                                elif widget_task[ii].mark == 2:  #表格
                                    pass
                                elif widget_task[ii].mark == 3:  #按钮
                                    #if widget_task[ii].cursor_index == 0:
                                        #widget_task[ii].select = True
                                    if widget_task[ii].select == True:
                                        color = '32'
                                    elif widget_task[ii].select == False:
                                        color = '30'
                                    if slen(widget_task[ii].text)>(self.width-2):
                                        text = re.findall(r'.{'+str(self.width-2)+r'}',widget_task[ii].text)
                                        print(color+"[1;31;40m%s"%text+color+"[0m")  
                                    elif widget_task[ii].way == 'L':
                                        printscreen = widget_task[ii].text+' '*(self.width-2-slen(widget_task[ii].text))
                                        print("║"+"\033[0;%sm%s\033[0m"%(color,printscreen)+"║")
                                    elif widget_task[ii].way == 'C':
                                        iii = int((self.width-2-slen(widget_task[ii].text))/2)
                                        inte = slen(widget_task[ii].text)
                                        printscreen = ' '*iii+widget_task[ii].text+color+'[0m'+' '*(self.width-2-iii-inte)
                                        print("║"+"\033[0;%sm%s\033[0m"%(color,printscreen)+"║")
                                    elif widget_task[ii].way == 'R':
                                        printscreen = (r'{:>'+str(self.width-2)+r'}').format(widget_task[ii].text)
                                        print("║"+"\033[0;%sm%s\033[0m"%(color,printscreen)+"║")
                                    Button_num+=1
                                    Frame.Button_num = Button_num
                                #del widget_task[ii]
                                #widget_a = len(widget_task)
                                a = 1
                                break
                        if a != 1:
                            print("║"+" "*(self.width-2)+"║")
                        a = 0
                    else:
                        print("║"+" "*(self.width-2)+"║")

class Line():
    def __init__(self,location):
        self.mark = 0
        self.location = location
class TextLine():
    def __init__(self,text,way,location):
        self.mark = 1
        self.text = text
        self.way = way
        self.location = location
class Form():
    def __init__(self,th,data,way,location):
        self.mark = 2
        self.th = th
        self.way = way
        self.location = location
class Button():
    def __init__(self,text,way,location,cursor_index):
        self.mark = 3
        self.select = False
        self.location = location
        self.text = text
        self.way = way
        self.cursor_index = cursor_index
    def onclick():
        pass
class Listener():
    def __init__(self,run):
        self.mark = 4
        self.running = False
    def run(self,Fram):
        c = cdll.LoadLibrary(os.getcwd()+"/getchar.so")
        while self.running:
            key = chr(c.get_char())
            #sys.stdout.write('%c'%string)
            #sys.stdout.flush()
            if key == "w":
                if Fram.cursor > 0 and Fram.Button_num != 1:
                    Fram.cursor -= 1
            if key == "s":
                if Fram.cursor < Fram.Button_num-1:
                    Fram.cursor += 1
            if key == "q": #q键退出
                sys.stdout.write('\n')
                break
            Fram.build(0)
#主框架-----------------------------------------------------------
class Frame():
    def __init__(self):
        self.windows = []
        self.Listener = Listener(False)
        self.cursor = 0
        self.Button_num = 0
    def add_window(self,wd):
        self.windows.append(wd)
    def listen(self,mark=0):
        self.Listener.running = True
        self.Listener.run(self)
    def build(self,mark=0):
        self.windows[mark].buildW(self)

#用例-----------------------------------------------
if __name__=="__main__":
    t = Frame()
    main_w = Window('主窗口',0)
    main_w.add_widget('TextLine',3,way='C',text='DUI测试界面')
    main_w.add_widget('line',4)
    main_w.add_widget('TextLine',5,text='你可以用w向上s向下,y键确认,q键退出')
    main_w.add_widget('Button',6,text='测试按钮1',cursor_index=0)
    main_w.add_widget('Button',7,text='测试按钮2',cursor_index=1)
    main_w.add_widget('Button',8,text='测试按钮3',cursor_index=2)
    t.add_window(main_w)
    t.build(0)
    t.listen(0)
