# -*- coding: utf-8 -*-

# 2019/1/18 0018 下午 1:19     

__author__ = 'RollingBear'

import configparser

'''读取配置文件'''


def loadConfig(name, key):
    config = configparser.ConfigParser()
    config.read("config.ini")

    return config.get(name, key)

    # LogListAddress = config.get("address", "LogListAddress")
    # RedPicAddress = config.get("address", "RedPicAddress")
    # GreenPicAddress = config.get("address", "GreenPicAddress")
    # YellowPicAddress = config.get("address", "YellowPicAddress")
    # LogoPicAddress = config.get("address", "LogoPicAddress")


def loadNameList():
    file = open(loadConfig("address", "NameListAddress"), encoding="utf-8-sig")
    ServiceNameList = []
    result = file.readlines()
    for count in range(len(result)):
        result[count] = result[count].replace("\n", "")
        result_1 = result[count].split(",")
        ServiceNameList.append(result_1[0])
        ServiceNameList.append(result_1[1])
        ServiceNameList.append(result_1[2])
    return ServiceNameList
