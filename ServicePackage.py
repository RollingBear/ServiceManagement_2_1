# -*- coding: utf-8 -*-

# 2019/1/18 0018 下午 12:54     

__author__ = 'RollingBear'

import ServiceOpt
import printComp
import time

'''名称'''
STATE_RUNNING = "已启动  "
STATE_STOPPED = "未启动  "
STATE_UNINSTALLED = "未安装  "

'''按钮服务'''


def ServiceAllStart(ServiceNameList):
    for count in range(int(len(ServiceNameList) / 3)):
        ServiceOpt.ServiceStart(ServiceNameList[int(count * 3)])


def ServiceAllStop(ServiceNameList):
    for count in range(int(len(ServiceNameList) / 3)):
        ServiceOpt.ServiceStop(ServiceNameList[int(count * 3)])


def openFileList(Address):
    ServiceOpt.openFile(Address)


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


def ButtonMenuReFresh(tk, ServiceNameList, LogListAddress, SetupAddress):
    for count in range(int(len(ServiceNameList) / 3)):
        printComp.printMenuButton(tk, ServiceNameList[int(count * 3 + 1)], ServiceNameList[int(count * 3)],
                                  count, 1,
                                  LogListAddress, ServiceNameList[int(count * 3 + 2)], SetupAddress)


def ReFreshStateThreading(tk, ServiceNameList, delay, GREEN, RED, YELLOW):
    while True:
        try:
            StateReFresh(tk, ServiceNameList, GREEN, RED, YELLOW)
        finally:
            print("state refresh")
        time.sleep(delay)


def ReFreshBtnMThreading(tk, ServiceNameList, LogListAddress, SetupAddress, delay):
    while True:
        try:
            ButtonMenuReFresh(tk, ServiceNameList, LogListAddress, SetupAddress)
        finally:
            print('Button Menu refresh')
        time.sleep(delay)
