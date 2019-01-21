# -*- coding: utf-8 -*-


# 2019/1/3 0003 下午 3:19     

__author__ = 'RollingBear'

from tkinter import *
import printComp
import ServicePackage
import LoadConfig
import threading

'''名称'''
START_ALL = "全部启动"
STOP_ALL = "全部停止"
LOG_LIST = "日志目录"
BLANK_1 = " "
BLANK_2 = "  "
BLANK_3 = "   "
BLANK_4 = "    "

'''启动服务'''


def start():
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
    InstallAddress = LoadConfig.loadConfig("address", "SetupAddress")

    # for count in range(int(len(ServiceNameList) / 3)):
    #     printComp.printMenuButton(myGui, ServiceNameList[int(count * 3 + 1)], ServiceNameList[int(count * 3)], count, 1,
    #                               LogListAddress, ServiceNameList[int(count * 3 + 2)], InstallAddress)

    printComp.printLabel(myGui, BLANK_4, int(len(ServiceNameList) / 3) + 1, 1, 1)
    printComp.printPNG(MESSAGE, int(len(ServiceNameList) / 3) + 2, 1, 100)
    printComp.printLabel(myGui, BLANK_4, int(len(ServiceNameList) / 3) + 3, 1, 1)

    printComp.printPNG(LOGO, int(len(ServiceNameList) / 3) + 4, 1, 1)
    printComp.printButton(myGui, START_ALL, ServiceNameList, int(len(ServiceNameList) / 3) + 4, 2, 1, LogListAddress)
    printComp.printButton(myGui, STOP_ALL, ServiceNameList, int(len(ServiceNameList) / 3) + 4, 3, 1, LogListAddress)
    printComp.printButton(myGui, LOG_LIST, None, int(len(ServiceNameList) / 3) + 4, 4, 1, LogListAddress)

    refreshStateThread = threading.Thread(target=ServicePackage.ReFreshStateThreading,
                                          args=(myGui, ServiceNameList, 2, GREEN, RED, YELLOW))
    refreshBtnMThread = threading.Thread(
        target=ServicePackage.ReFreshBtnMThreading, args=(myGui, ServiceNameList, LogListAddress, InstallAddress, 5))

    refreshStateThread.daemon = True
    refreshBtnMThread.daemon = True

    refreshStateThread.start()
    refreshBtnMThread.start()

    myGui.update_idletasks()

    width = 430
    SetX = (myGui.winfo_screenwidth() - width) / 2
    height = int(len(ServiceNameList)) * 26 / 3 + 133
    SetY = (myGui.winfo_screenheight() - height) / 2
    myGui.geometry("%dx%d+%d+%d" % (width, height, SetX, SetY))
    myGui.deiconify()

    myGui.mainloop()


if __name__ == '__main__':
    start()
