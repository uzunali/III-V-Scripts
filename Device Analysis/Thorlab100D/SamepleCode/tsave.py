# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:59:14 2021

@author: ali.uzun
"""

from datetime import datetime
from ctypes import cdll,c_long, c_ulong, c_uint32,byref,create_string_buffer,c_bool,c_char_p,c_int,c_int16,c_double, sizeof, c_voidp
from TLPM import TLPM
import time


tlPM = TLPM()


tlPM.close()