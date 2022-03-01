import sys
sys.path.append("/Users/au/Desktop/Tyndall/Scripts/Python/III-V Scripts/src")

from OpenFile import OpenFile
from Data_Analysis import Data_Analysis
import pandas as pd

da = Data_Analysis()
of = OpenFile()



f = "Detector Check Cleaved Facet 2.5um LI.csv"

cl = ["2.5","3.0","3.5"]
mtype = ["LI","VI"]

# dictionary of lists 
row_number = 0  

cl_index = 2
fl_index = 0


f = "Detector Check Cleaved Facet %sum %s.csv" % (cl[cl_index],mtype[fl_index])
full_filename = "/Users/au/Desktop/Tyndall/Scripts/Python/III-V Scripts/Device Analysis/Data/%s"%(f)
print(full_filename)

df = pd.read_csv (full_filename)
#print(mtype[0])
print(f)
#print(df.columns)
Responsivity = 0.75
mtype = ["Keithley_ChB (R %s)"%Responsivity,"Keithley_ChB & PM","Newport_USB-PM"]


try:
    x = df["Current (mA)"]
except:
    print("X")

ys = []
line_label = []
x_max = 150
for index,i in enumerate(df.columns[1:]):
    print(i)
    try:
        y = df[i]*1e3
        if(i == "Newport_Keithley_ChB"):
            y = df[i]*1e3/Responsivity
            print("CCC")
        
        #y = df[label][:x_max]
        #print(len(y))
        ys.append(y)
        #t=label.split("_")[1:] # for cleaved facet 

        line_label.append(mtype[index])
    except:
        print("Y")


y_label_dict = {0:"Power /facet (mW)", 1:"Total Power (mW)"}
x_label = df.columns[0]
if(mtype[fl_index] == "LI"): y_label = y_label_dict[0]
else: y_label = "Voltage (V)"
y_label = y_label_dict[0]
#print("Selected index")
plot_title = ""#"Etched Facet Facet"
legend_font = 10
label_fontsize = 14
lwidth = 3
da.plot_XYs(line_label,x_label, y_label, x, ys,plot_title=plot_title,legend_font=legend_font, label_fontsize=label_fontsize,lwidth=lwidth)


