# -*- coding: utf-8 -*-

# 2019/1/18 0018 下午 12:54     

__author__ = 'RollingBear'

from tkinter import *
import ServiceOpt
import printComp
import configparser
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

SERVICE_NOT_INSTALL = "服务未安装"
STATE_RUNNING = "已启动"
STATE_STOPPED = "未启动"
STATE_UNINSTALLED = "未安装"

'''按钮服务'''


def ServiceAllStart(tk, ServiceNameList):
    for count in range(int(len(ServiceNameList) / 2)):
        ServiceOpt.ServiceStart(ServiceNameList[int(count * 2)])
        # ServiceState(tk, count, 3, 1, ServiceNameList[int(count * 2)])


def ServiceAllStop(tk, ServiceNameList):
    for count in range(int(len(ServiceNameList) / 2)):
        ServiceOpt.ServiceStop(ServiceNameList[int(count * 2)])
        # ServiceState(tk, count, 3, 1, ServiceNameList[int(count * 2)])


def openFileList(Address):
    ServiceOpt.openFile(Address)


'''加载服务状态'''

#
# def ServiceState(tk, count, column, columnspan, ServiceName):
#     FLAG = ServiceOpt.getServiceState(ServiceName)
#     if FLAG == 1:
#         printComp.printPNG(GREEN, count, column, columnspan)
#         printComp.printLabel(tk, STATE_RUNNING, count, column + 1, columnspan)
#         return True
#     elif FLAG == 0:
#         printComp.printPNG(RED, count, column, columnspan)
#         printComp.printLabel(tk, STATE_STOPPED, count, column + 1, columnspan)
#         return True
#     elif FLAG == -1:
#         printComp.printPNG(YELLOW, count, column, columnspan)
#         printComp.printLabel(tk, STATE_UNINSTALLED, count, column + 1, columnspan)
#         return False
'''状态刷新'''


def StateReFresh(tk, ServiceNameList, GREEN, RED, YELLOW):
    for count in range(int(len(ServiceNameList) / 3)):
        FLAG = ServiceOpt.getServiceState(ServiceNameList[int(count * 3)])
        if FLAG == 1:
            printComp.printPNG(GREEN, count, 3, 1)
            printComp.printLabel(tk, STATE_RUNNING, count, 4, 1)
        elif FLAG == 0:
            printComp.printPNG(RED, count, 3, 1)
            printComp.printLabel(tk, STATE_STOPPED, count, 4, 1)
        elif FLAG == -1:
            printComp.printPNG(YELLOW, count, 3, 1)
            printComp.printLabel(tk, STATE_UNINSTALLED, count, 4, 1)


def ReFreshThreading(tk, ServiceNameList, delay, GREEN, RED, YELLOW):
    while True:
        try:
            StateReFresh(tk, ServiceNameList, GREEN, RED, YELLOW)
        finally:
            print("run refresh")
        time.sleep(delay)
