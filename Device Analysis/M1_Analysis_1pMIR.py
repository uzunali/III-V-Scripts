import pandas as pd
from Data_Analysis import Data_Analysis
from OpenFile import OpenFile

da = Data_Analysis()
of = OpenFile()

fl = "LI"
f = "Detector Check Cleaved Facet 2.5um %s.csv" % fl

filename = "/Users/au/Desktop/Tyndall/Scripts/Python/III-V Scripts/Device Analysis/Data/" % f
#filename = "/Users/au/Desktop/Measurements New/Etched Facet Device/CL2mm/" + f

#filename = of.get_signle_file()
df = pd.read_table(filename, sep=",")

x_max = 160
x = df['Current'][:x_max]
ys = []
#print(len(x))

y_label_dict = {0:"Power /facet (mW)", 1:"Total Power (mW)"}
x_label = df.columns[0]
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
                sp = "-"
                t = sp.join(t[1:])
                #t=label.split("_")[1] # for cleaved facet 
                #t=label.split("_")
                #t = t[1] + t[3]

                line_label.append(t)
        except:
            print("NNN")

def get_selected():
    for i in ys_index:
        try:
            label = df.columns[i]
            y = df[label][:x_max]
            #print(len(y))
            ys.append(y)
            #t=label.split("_")[1:] # for cleaved facet 
            t = label.split("_")
            sp = "-"
            t = sp.join(t[1:])
            #t = t[3]
            #t = t[2] # 
            line_label.append(t)
        except:
            print("NNN")

#select_one_by_one()
get_selected()

print("Selected index")
print(y_i)
plot_title = ""#"Etched Facet Facet"
legend_font = 10
label_fontsize = 14
da.plot_XYs(line_label,x_label, y_label, x, ys,plot_title=plot_title,legend_font=legend_font, label_fontsize=label_fontsize)


