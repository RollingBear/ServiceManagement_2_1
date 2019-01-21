# -*- coding: utf-8 -*-

# 2019/1/18 0018 下午 12:51     

__author__ = 'RollingBear'

from tkinter import *
import ServiceOpt
import ServicePackage
import LoadConfig
import time

'''名称'''
START = "启动"
STOP = "停止"
RE_START = "重启"
SET_START_AUTO = "打开自启"
SET_START_DEMAND = "关闭自启"
SET_START_DISABLED = "禁用服务"
INSTALL = "安装服务"
UNINSTALL = "卸载服务"
LOG_FILE = "日志"
LOG_LIST = "日志目录"
START_ALL = "全部启动"
STOP_ALL = "全部停止"
LOG_LIST = "日志目录"

'''添加下拉菜单'''


def printMenuButton(tk, text, mes, count, column, LogAddress, LogFile, InstallAddress):
    FLAG = ServiceOpt.getServiceState(mes)

    # 判断地址
    SetupAddress = InstallAddress
    if mes == 'Face_Nginx':
        SetupAddress = LoadConfig.loadConfig("file_address", "NginxWebAddress")
    elif mes == 'Face_Mosquitto':
        SetupAddress = LoadConfig.loadConfig("file_address", "MosquittoAddress")

    btn = Menubutton(tk, text=text, anchor='w', height=1, relief=FLAT, activeforeground="blue")
    btn.grid(row=count, column=column, sticky=W)

    fileMenu = Menu(btn, tearoff=False)

    # 启动服务
    fileMenu.add_command(label=START, command=lambda: btnStart(mes))

    def btnStart(mes):
        ServiceOpt.ServiceStart(mes)
        fileMenu.entryconfig(START, state=DISABLED)

    # 停止服务
    fileMenu.add_command(label=STOP, command=lambda: btnStop(mes))

    def btnStop(mes):
        ServiceOpt.ServiceStop(mes)
        fileMenu.entryconfig(STOP, state=DISABLED)

    # 重启服务
    fileMenu.add_command(label=RE_START, command=lambda: btnReStart(mes))

    def btnReStart(mes):
        ServiceOpt.ServiceReStart(mes)
        fileMenu.entryconfig(RE_START, state=DISABLED)

    fileMenu.add_separator()

    # 打开服务日志
    fileMenu.add_command(label=LOG_FILE, command=lambda: btnLogFile(LogAddress, LogFile))

    def btnLogFile(LogAddress, LogFile):
        ServiceOpt.openNoteByName(LogAddress, LogFile)
        fileMenu.entryconfig(LOG_FILE, state=DISABLED)

    fileMenu.add_separator()

    # 打开服务自启
    fileMenu.add_command(label=SET_START_AUTO, command=lambda: btnSetState(mes, SET_START_AUTO, "auto"))
    # 关闭服务自启
    fileMenu.add_command(label=SET_START_DEMAND, command=lambda: btnSetState(mes, SET_START_DEMAND, "demand"))
    # 禁用服务
    fileMenu.add_command(label=SET_START_DISABLED, command=lambda: btnSetState(mes, SET_START_DISABLED, "disabled"))

    def btnSetState(mes, label, STATE):
        ServiceOpt.ServiceSetStartAuto(mes, STATE)
        fileMenu.entryconfig(label, state=DISABLED)

    fileMenu.add_separator()

    # 安装服务
    fileMenu.add_command(label=INSTALL, command=lambda: btnSetup(SetupAddress, mes))

    def btnSetup(SetupAddress, mes):
        ServiceOpt.openSetup(SetupAddress, mes)
        fileMenu.entryconfig(INSTALL, state=DISABLED)

    # 卸载服务
    fileMenu.add_command(label=UNINSTALL, command=lambda: btnDelete(mes))

    def btnDelete(mes):
        ServiceOpt.ServiceDelete(mes)
        fileMenu.entryconfig(UNINSTALL, state=DISABLED)

    if LogFile == '':
        fileMenu.entryconfig(LOG_FILE, state=DISABLED)

    if FLAG == -1:
        for index in [START, STOP, RE_START, SET_START_AUTO, SET_START_DEMAND, SET_START_DISABLED, UNINSTALL]:
            fileMenu.entryconfig(index, state=DISABLED)
    elif FLAG == 0:
        fileMenu.entryconfig(STOP, state=DISABLED)
        fileMenu.entryconfig(INSTALL, state=DISABLED)
    elif FLAG == 1:
        fileMenu.entryconfig(START, state=DISABLED)
        fileMenu.entryconfig(INSTALL, state=DISABLED)

    btn.config(menu=fileMenu)


def printButton(tk, text, mes, row, column, columnspan, Address):
    if text == START_ALL:
        btn = Button(tk, text=text, width=8, height=1, activeforeground="blue",
                     command=lambda tk=tk, List=mes: ServicePackage.ServiceAllStart(List))
    elif text == STOP_ALL:
        btn = Button(tk, text=text, width=8, height=1, activeforeground="blue",
                     command=lambda tk=tk, List=mes: ServicePackage.ServiceAllStop(List))
    elif text == LOG_LIST:
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
