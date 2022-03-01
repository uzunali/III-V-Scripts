# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:01:41 2021

@author: ali.uzun
"""

from ThorlabsPM100 import ThorlabsPM100, USBTMC

#inst = USBTMC("USB0::0x1313::0x8078::::INSTR")
#(inst)

#power_meter = ThorlabsPM100(inst = inst)


import pyvisa


rm = pyvisa.ResourceManager()


resources = rm.list_resources()



inst = rm.open_resource("USB0::0x1313::0x8078::::INSTR")
