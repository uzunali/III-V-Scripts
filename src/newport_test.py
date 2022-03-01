# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:49:05 2021

@author: ali
"""

import win32gui
import win32com.client
import time
import traceback


OphirCOM = win32com.client.Dispatch("OphirLMMeasurement.CoLMMeasurement")
# Stop & Close all devices
OphirCOM.StopAllStreams() 
OphirCOM.CloseAll()
# Scan for connected Devices
DeviceList = OphirCOM.ScanUSB()
print(DeviceList)
