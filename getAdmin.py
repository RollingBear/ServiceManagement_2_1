from __future__ import print_function
# -*- coding: utf-8 -*-

#   2019/1/22 0022 上午 11:37     

__author__ = 'RollingBear'

import ctypes
import sys
import ServiceManagementMain

def is_admin():

    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():

    ServiceManagementMain.start()

else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    # else:
    #     ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)