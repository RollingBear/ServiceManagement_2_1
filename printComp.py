# -*- coding: utf-8 -*-

# 2019/1/18 0018 下午 12:51     

__author__ = 'RollingBear'

from tkinter import *
import ServiceOpt
import ServicePackage

'''名称'''
START = "启动"
START_ALL = "全部启动"
STOP = "停止"
STOP_ALL = "全部停止"
RE_START = "重启"
SET_START_AUTO = "打开自启"
SET_START_DEMAND = "关闭自启"
SET_START_DISABLED = "禁用服务"
INSATLL = "安装服务"
UNINSTALL = "卸载服务"
LOG_FILE = "日志"
LOG_LIST = "日志目录"
INSTALL_LIST = "安装目录"

SERVICE_NOT_INSTALL = "服务未安装"
STATE_RUNNING = "已启动"
STATE_STOPPED = "未启动"
STATE_UNINSTALLED = "未安装"


def printMenuButton(tk, text, mes, count, column, LogAddress, LogFile, SetupAddress):
    btn = Menubutton(tk, text=text, anchor='w', height=1, relief=FLAT, activeforeground="blue")
    btn.grid(row=count, column=column, sticky=W)
    fileMenu = Menu(btn, tearoff=False)
    FLAG = ServiceOpt.getServiceState(mes)
    fileMenu.add_radiobutton(label=START, value=1, command=lambda: btnStart(mes))
    if FLAG == -1:
        fileMenu.entryconfig(1, state=DISABLED)
    if FLAG == 1:
        fileMenu.entryconfig(1, state=DISABLED)

    def btnStart(mes):
        ServiceOpt.ServiceStart(mes)
        printMenuButton(tk, text, mes, count, column, LogAddress, LogFile, SetupAddress)

    fileMenu.add_radiobutton(label=STOP, value=2, command=lambda: btnStop(mes))
    if FLAG == -1:
        fileMenu.entryconfig(2, state=DISABLED)
    if FLAG == 0:
        fileMenu.entryconfig(2, state=DISABLED)

    def btnStop(mes):
        ServiceOpt.ServiceStop(mes)
        printMenuButton(tk, text, mes, count, column, LogAddress, LogFile, SetupAddress)

    fileMenu.add_radiobutton(label=RE_START, value=3, command=lambda: ServiceOpt.ServiceReStart(mes))
    if FLAG == -1:
        fileMenu.entryconfig(3, state=DISABLED)
    fileMenu.add_radiobutton(label=LOG_FILE, value=4, command=lambda: ServiceOpt.openNoteByName(LogAddress, LogFile))
    if LogFile == '':
        fileMenu.entryconfig(4, state=DISABLED)
    fileMenu.add_radiobutton(label=SET_START_AUTO, value=5, command=lambda: ServiceOpt.ServiceSetStartAuto(mes, "auto"))
    if FLAG == -1:
        fileMenu.entryconfig(5, state=DISABLED)
    fileMenu.add_radiobutton(label=SET_START_DEMAND, value=6,
                             command=lambda: ServiceOpt.ServiceSetStartAuto(mes, "demand"))
    if FLAG == -1:
        fileMenu.entryconfig(6, state=DISABLED)
    fileMenu.add_radiobutton(label=SET_START_DISABLED, value=7,
                             command=lambda: ServiceOpt.ServiceSetStartAuto(mes, "disabled"))
    if FLAG == -1:
        fileMenu.entryconfig(7, state=DISABLED)
    fileMenu.add_radiobutton(label=INSATLL, value=8, command=lambda: btnSetup(SetupAddress, mes))
    if FLAG != -1:
        fileMenu.entryconfig(8, state=DISABLED)

    def btnSetup(SetupAddress, mes):
        ServiceOpt.openSetup(SetupAddress, mes)
        printMenuButton(tk, text, mes, count, column, LogAddress, LogFile, SetupAddress)

    fileMenu.add_radiobutton(label=UNINSTALL, value=9, command=lambda: btnDelete(mes))
    if FLAG == -1:
        fileMenu.entryconfig(9, state=DISABLED)

    def btnDelete(mes):
        ServiceOpt.ServiceDelete(mes)
        printMenuButton(tk, text, mes, count, column, LogAddress, LogFile, SetupAddress)

    btn.config(menu=fileMenu)


def printButton(tk, text, mes, row, column, columnspan, Address):
    if text == START_ALL:
        btn = Button(tk, text=text, width=8, height=1, activeforeground="blue",
                     command=lambda tk=tk, List=mes: ServicePackage.ServiceAllStart(tk, List))
    elif text == STOP_ALL:
        btn = Button(tk, text=text, width=8, height=1, activeforeground="blue",
                     command=lambda tk=tk, List=mes: ServicePackage.ServiceAllStop(tk, List))
    elif text == LOG_LIST:
        btn = Button(tk, text=text, width=8, height=1, activeforeground="blue",
                     command=lambda: ServicePackage.openFileList(Address))
    elif text == INSTALL_LIST:
        btn = Button(tk, text=text, width=8, height=1, activeforeground="blue",
                     command=lambda: ServicePackage.openFileList(Address))
    btn.grid(row=row, column=column, columnspan=columnspan)
    btn.bind("<Enter>", lambda event: event.widget.config(fg="blue"))
    btn.bind("<Leave>", lambda event: event.widget.config(fg="black"))


'''图片'''


def printPNG(photo, row, column, columnspan):
    label = Label(image=photo)
    label.image = photo
    label.grid_forget()
    label.grid(row=row, column=column, columnspan=columnspan)


'''标签'''


def printLabel(tk, mes, row, column, columnspan, sticky=W):
    Label(tk, text=mes, anchor=NW).grid(row=row, column=column, columnspan=columnspan, sticky=sticky)
