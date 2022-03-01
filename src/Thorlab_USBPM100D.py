# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:15:06 2021

@author: ali.uzun
"""

from datetime import datetime
from ctypes import cdll,c_long, c_ulong, c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_int16,c_double, sizeof, c_voidp
from TLPM import TLPM
import time

class Thorlab_100D():
    def __init__(self):
        
        self.resourceName = create_string_buffer(1024)
              
            
    def Initialize_connection(self):
        tlPM = TLPM()
        deviceCount = c_uint32()
        tlPM.findRsrc(byref(deviceCount))
        
        print("devices found: " + str(deviceCount.value))
        
        self.resourceName = create_string_buffer(1024)
        
        for i in range(0, deviceCount.value):
            tlPM.getRsrcName(c_int(i), self.resourceName)
            print(c_char_p(self.resourceName.raw).value)
            break
        
        tlPM.close()
    
    def get_power_reading(self):
        tlPM = TLPM()
        tlPM.open(self.resourceName, c_bool(True), c_bool(True))
    
        time.sleep(0.5)
        power =  c_double()
        tlPM.measPower(byref(power))
        #power_measurements.append(power.value)
        #times.append(datetime.now())
        print(power.value)
        time.sleep(0)
    
        tlPM.close()
    
    def set_wavelength(self, wavelength):
        tlPM = TLPM()
        tlPM.open(self.resourceName, c_bool(True), c_bool(True))
        
        wavelength = c_double(wavelength)
        tlPM.setWavelength(byref(wavelength))
    
        tlPM.close()
        
    def get_wavelength(self):
        tlPM = TLPM()
        tlPM.open(self.resourceName, c_bool(True), c_bool(True))
        
        wavelength = c_double()
        TLPM_ATTR_SET_VAL = c_int16(0)
        wl = tlPM.getWavelength(byref(TLPM_ATTR_SET_VAL,wavelength))
        print(wl)
    
        tlPM.close()

def v1():
    
    tlPM = TLPM()
    #resourceName = create_string_buffer(b"COM1::115200")
    #print(c_char_p(resourceName.raw).value)
    resourceName = create_string_buffer(1024)
    tlPM.open(resourceName, c_bool(True), c_bool(True))
    
    message = create_string_buffer(1024)
    tlPM.getCalibrationMsg(message)
    print(c_char_p(message.raw).value)
    
    wavelength = c_double(1500)
    tlPM.setWavelength(byref(wavelength))
    
    # # set current range
    # current_to_Measure = c_double(1)
    # tlPM.setCurrentRange(current_to_Measure)
    
    time.sleep(5)
    
    power_measurements = []
    times = []
    count = 0
    while count < 20:
        power =  c_double()
        tlPM.measPower(byref(power))
        power_measurements.append(power.value)
        times.append(datetime.now())
        print(power.value)
        count+=1
        time.sleep(1)
    
    wavelength = c_double()
    TLPM_ATTR_SET_VAL = c_int16(0)
    tlPM.getWavelength(byref(TLPM_ATTR_SET_VAL,wavelength))
    
    tlPM.close()
    print('End program')
