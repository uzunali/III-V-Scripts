import sys
#sys.path.append("/Users/au/Desktop/Tyndall/Scripts/Python/III-V Scripts/src")
sys.path.append("\\\\FS1\Docs2\\ali.uzun\\My Documents\\My Files\\Scripts\\Python\\III-V Scripts-20220225\\src")

import pandas as pd
from Data_Analysis import Data_Analysis
from OpenFile import OpenFile

da = Data_Analysis()
fl = OpenFile()

fl = "/Users/au/Desktop/Tyndall/Measurements/Caladan/Caladan20-21/EF-MIR2020/QDL on AL2O3/SOI3/2022-02-09do6209_QDL_on_40nm-AL2O3_on SOI3_LI.csv"
fl = "\\\\FS1\Docs2\\ali.uzun\\My Documents\\My Files\\Measurements\\Caladan\\Caladan20-21\\EF-MIR2020\\Run-2 do6209\\do6209 QDL Coupon\AU-2-1\\2022-02-28\\R1do6209_2mm_1pMIR_RW_Xum_MIR_Xum_D4_Photocurrent.csv"
plot_title = ""#"Etched Facet Facet"
legend_font = 10
label_fontsize = 18
lwidth = 3

filename = da.plot_XmY(is_LI=False,y_scale = 1e0,legend_font=legend_font, label_fontsize=label_fontsize, lwidth=lwidth)


