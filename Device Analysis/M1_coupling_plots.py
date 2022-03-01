#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from Data_Analysis import Data_Analysis
from OpenFile import OpenFile

da = Data_Analysis()
of = OpenFile()

filename = "/Users/au/Desktop/Tyndall/Measurements/Caladan/Caladan20-21/In-Out Grating Coupling/2022-01-06 1260-1360 Sweep_Caladan_metal_S1_s2.csv"
fl = "AU21_R2do6209_D2_2"
fl = "AU21_R2do6209_D3-2"
fl = "AU21_R2do6209_D8_photocurrent-2"
#fl = "AU21_R2do6209_D8"
#filename = "/Users/au/Desktop/Tyndall/Measurements/Caladan/Caladan20-21/EF-MIR2020/Run-2 do6209/do6209_QDL Coupon/AU-2-1/2022-01-07/%s.csv"%fl

df = pd.read_table(filename, sep=",")

x_col = "Current"
x_col = "Wavelength (nm)"
x = df[x_col]

y_col = "Power (mW)"
R = 0.65
R = 1
coef = 1e6

y = df[y_col]*coef/R

x_label = df.columns[0]
y_label = "WG Coupled Power (%sW)" % '\u03BC' # "m"

plot_title = ""#"Etched Facet Facet"
legend_font = 10
label_fontsize = 18
lwidth = 3
line_label = [""]
da.plot_XYs(line_label,x_label, y_label, x, [y] ,plot_title=plot_title,legend_font=legend_font, label_fontsize=label_fontsize, lwidth=lwidth)

