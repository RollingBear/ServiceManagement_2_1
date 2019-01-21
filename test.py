# -*- coding: utf-8 -*-


# 2019/1/10 0010 下午 4:38

__author__ = 'RollingBear'

import configparser
import os
import sys
import time
import threading

#
# config = configparser.ConfigParser()
# config.read("config.ini")
#
# print(config.get("name", "ServiceName"))
# print(config.get("name", "ServiceName").split(', '))
#
# Address = "Done\pack\pack"
# test = "..\..\..\pack"
# test2 = "..\..\pack"
# test3 = "..\pack"
#
# now = os.getcwd()
# print(now)
# father = os.path.abspath(os.path.dirname(now) + os.path.sep + ".")
# print(father)
# grand = os.path.abspath(os.path.dirname(now) + os.path.sep + "..")
# print(grand)
# os.popen("start " + os.path.abspath(os.path.dirname(now)+os.path.sep+"..") + Address)

# print(test.count("..\\"))
# print(test2.count("..\\"))
# print(test3.count("..\\"))
# print(test.replace("..\\", ""))
# print("~" * test.count("..\\") + test.replace("..\\", ""))
# Address_test = "..\..\Done\pack\pack"
#
# print("start " + os.path.abspath(
#     os.path.dirname(os.getcwd()) + os.path.sep + ("." * Address_test.count("..\\"))) + "\\" + Address_test.replace(
#     "..\\",
#     ""))
#
# os.popen("start " + os.path.abspath(Address_test))
#
# try:
#     _thread.start_new_thread(ReFreshThread, (myGui, ServiceNameList, 2))
# except:
#     print('Thread start Error')
#
# ServiceName = 'Face_TrailsMerge'
# print(ServiceName)
# SetupAddress = '..\..\\nginx-1.14.0'
# print("sc create " + ServiceName + ' binPath="' + SetupAddress + "\\" + ServiceName('Face_', 'WinSW_') + '.exe"')
#
# import LoadConfig
#
# file = open(LoadConfig.loadConfig("address", "NameListAddress"), encoding="utf-8-sig")
# ServiceNameList = []
# result = file.readlines()
# for count in range(len(result)):
#     result[count] = result[count].replace("\n", "")
#     result_1 = result[count].split(",")
#     ServiceNameList.append(result_1[0])
#     ServiceNameList.append(result_1[1])
#     if result_1[2] == '':
#         result_1[2].replace('', 'None')
#     ServiceNameList.append(result_1[2])
# print(ServiceNameList)
#
# for i in range(1, 10):
#     print(i)
