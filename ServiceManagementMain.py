# -*- coding: utf-8 -*-


# 2019/1/3 0003 下午 3:19     

__author__ = 'RollingBear'

from tkinter import *
import ServiceOpt
import printComp
import ServicePackage
import LoadConfig
import time
import threading

'''名称'''
START = "启动"
START_ALL = "全部启动"
STOP = "停止"
STOP_ALL = "全部停止"
RE_START = "重启"
SET_START_AUTO = "打开自启"
SET_START_ALL_AUTO = "打开全部自启"
SET_START_DEMAND = "关闭自启"
SET_START_ALL_DEMAND = "关闭全部自启"
SET_START_DISABLED = "禁用服务"
SET_START_ALL_DISABLED = "禁用全部服务"
LOG_FILE = "日志"
LOG_LIST = "日志目录"
RE_FRESH_STATE = "刷新状态"
INSTALL_LIST = "安装目录"

SERVICE_NOT_INSTALL = "服务未安装"
STATE_RUNNING = "已启动"
STATE_STOPPED = "未启动"
STATE_UNINSTALLED = "未安装"

BLANK_1 = " "
BLANK_2 = "  "
BLANK_3 = "   "
BLANK_4 = "    "

'''启动服务'''


def start():
    global GREEN, RED, YELLOW, LOGO
    myGui = Tk(className="服务管理")
    myGui.withdraw()
    myGui.resizable(width=False, height=False)

    GREEN = PhotoImage(file=LoadConfig.loadConfig("address", "GreenPicAddress"))
    RED = PhotoImage(file=LoadConfig.loadConfig("address", "RedPicAddress"))
    YELLOW = PhotoImage(file=LoadConfig.loadConfig("address", "YellowPicAddress"))
    LOGO = PhotoImage(file=LoadConfig.loadConfig("address", "LogoPicAddress"))
    MESSAGE = PhotoImage(file=LoadConfig.loadConfig("address", "MessagePicAddress"))
    ServiceNameList = LoadConfig.loadNameList()
    LogListAddress = LoadConfig.loadConfig("address", "LogListAddress")
    SetupAddress = LoadConfig.loadConfig("address", "SetupAddress")

    for count in range(int(len(ServiceNameList) / 3)):
        printComp.printMenuButton(myGui, ServiceNameList[int(count * 3 + 1)], ServiceNameList[int(count * 3)], count, 1,
                                  LogListAddress, ServiceNameList[int(count * 3 + 2)], SetupAddress)

    printComp.printLabel(myGui, BLANK_4, int(len(ServiceNameList) / 3) + 1, 1, 1)
    printComp.printPNG(MESSAGE, int(len(ServiceNameList) / 3) + 2, 1, 100)
    printComp.printLabel(myGui, BLANK_4, int(len(ServiceNameList) / 3) + 3, 1, 1)

    printComp.printPNG(LOGO, int(len(ServiceNameList) / 3) + 4, 1, 1)
    printComp.printButton(myGui, START_ALL, ServiceNameList, int(len(ServiceNameList) / 3) + 4, 2, 1, LogListAddress)
    printComp.printButton(myGui, STOP_ALL, ServiceNameList, int(len(ServiceNameList) / 3) + 4, 3, 1, LogListAddress)
    printComp.printButton(myGui, LOG_LIST, None, int(len(ServiceNameList) / 3) + 4, 4, 1, LogListAddress)
    printComp.printButton(myGui, INSTALL_LIST, None, int(len(ServiceNameList) / 3) + 4, 5, 1, SetupAddress)

    refreshThread = threading.Thread(target=ServicePackage.ReFreshThreading,
                                     args=(myGui, ServiceNameList, 2, GREEN, RED, YELLOW))
    refreshThread.start()

    myGui.update_idletasks()

    SetX = (myGui.winfo_screenwidth() - myGui.winfo_reqwidth()) / 2
    SetY = (myGui.winfo_screenheight() - myGui.winfo_reqheight()) / 2
    myGui.geometry("%dx%d+%d+%d" % (myGui.winfo_reqwidth() + 8, myGui.winfo_reqheight(), SetX, SetY))
    # myGui.deiconify()
    myGui.mainloop()


if __name__ == '__main__':
    start()
