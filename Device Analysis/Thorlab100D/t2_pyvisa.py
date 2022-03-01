# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:05:14 2021

@author: ali.uzun
"""

#import visa
import pyvisa
# from ThorlabsPM100 import ThorlabsPM100
import time

rm = pyvisa.ResourceManager()
resources = rm.list_resources()
print(resources)
