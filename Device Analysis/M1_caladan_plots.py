import sys
sys.path.append("/Users/au/Desktop/Tyndall/Scripts/Python/III-V Scripts/src")

import pandas as pd
from Data_Analysis import Data_Analysis
from OpenFile import OpenFile

da = Data_Analysis()
of = OpenFile()

fl = "LI"
dv = ["CF","EF","1pMIR"]
ref = dv[2]

if(ref == "CF"):
    f = "do6209_FP_Device_2mm_CF_%s.csv" % fl 
    filename = "/Users/au/Desktop/Measurements New/Cleaved Facet Device/CL2mm/" + f
elif(ref == "EF"):
    #f = "EF_1mm_%s.csv" % fl
    #f = "do6209_FP_on_GaAs_EF_1.5mm_%s.csv" % fl
    f = "do6209_FP_on_GaAs_EF_2mm_MirrorCleaved_%s.csv" % fl
    filename = "/Users/au/Desktop/Measurements New/Etched Facet Device/CL2mm/" + f
elif(ref == "1pMIR"):
    f = "2021-07-20 1PMIR_2mm_"+ "%s.csv" % fl
    filename = "/Users/au/Desktop/Measurements New/1pMIR Device/CL2mm/" + f

print(filename)

#filename = of.get_signle_file()
df = pd.read_table(filename, sep=",")
if (ref == "CF"):
    ys_index = [5,6,8] # 4--2.5um, 7--4um cleaved facet
elif(ref == "EF"):
    #ys_index = [4, 5, 10, 13] # etchec facet 1mm
    ys_index = [1,3, 6, 11, 12, 17] # etchec facet 1.5mm
    ys_index = [1, 3, 7] # etchec facet 2mm
elif(ref == "1pMIR"):
    i=4
    ys_index = [i, i+4, i+4*2, i+4*3, i+4*4]#[1, 7, 10] # MIR  2mm
x_max = 160
x = df['Current'][:x_max]
ys = []
print(len(x))

y_label_dict = {0:"Power /facet (mW)", 1:"Total Power (mW)"}
x_label = df.columns[0] + "(mA)"
if(fl == "LI"): y_label = y_label_dict[0]
else: y_label = "Voltage (V)"

y_i = []
line_label = []
def select_one_by_one():
    for i in range(1,len(df.columns)):
        
        try:
            label = df.columns[i]
            y = df[label][:x_max]
            da.plot_XY(label, x_label, y_label, x, [y], plot_title="", range = (20, None), show_slope = False)
            is_add = input("Add the device %s (y or n)"%i)
            if (is_add=="y"):
                ys.append(y)
                y_i.append(i)
                t = label.split("_")
                print(t)
                #sp = "-"
                #t = sp.join(t[1:])
                #t=label.split("_")[1] # for cleaved facet 
                #t=label.split("_")
                t = t[1] + t[3]

                line_label.append(t)
        except:
            print("NNN")
    ys_index = y_i

def get_selected():
    for i in ys_index:
        print(df.columns[i])
        try:
            label = df.columns[i]
            y = df[label][:x_max]
            #print(len(y))
            ys.append(y)
            t=label.split("_")
            if (ref == "CF"):
                t=t[-1] # for cleaved facet 
            elif(ref == "EF"):
                sp = "-"
                t = sp.join(t[2:5]) # EF
            elif(ref == "1pMIR"):
                sp = "-"
                t = sp.join(t[1:]) # 1pMIR

            line_label.append(t)
        except:
            print("NNN")

#select_one_by_one()
get_selected()

print("Selected index")
print(ys_index)
plot_title = ""#"Etched Facet Facet"
legend_font = 14
label_fontsize = 18
lwidth = 3
da.plot_XYs(line_label,x_label, y_label, x, ys,plot_title=plot_title,legend_font=legend_font, label_fontsize=label_fontsize, lwidth=lwidth)


