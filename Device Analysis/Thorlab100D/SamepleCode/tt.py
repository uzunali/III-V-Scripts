# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:29:31 2021

@author: ali.uzun
"""

from datetime import datetime
from ctypes import cdll,c_long, c_ulong, c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_int16,c_double, sizeof, c_voidp
from TLPM import TLPM
import time


tlPM = TLPM()


tlPM.close()
deviceCount = c_uint32()
tlPM.findRsrc(byref(deviceCount))

print("devices found: " + str(deviceCount.value))

resourceName = create_string_buffer(1024)


tlPM.getRsrcName(c_int(0), resourceName)
print(c_char_p(resourceName.raw).value)


tlPM.close()

tlPM = TLPM()
#resourceName = create_string_buffer(b"COM1::115200")
#print(c_char_p(resourceName.raw).value)
tlPM.open(resourceName, c_bool(True), c_bool(True))

tlPM.setWavelength(1100)

time.sleep(5)

power_measurements = []
times = []
count = 0
while count < 10:
    power =  c_double()
    tlPM.measPower(byref(power))
    power_measurements.append(power.value)
    times.append(datetime.now())
    print(power.value)
    count+=1
    time.sleep(1)

#tlPM.getWavelength()
tlPM.close()
print('End program')
