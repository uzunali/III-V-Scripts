import pandas as pd
from Data_Analysis import Data_Analysis
from OpenFile import OpenFile

da = Data_Analysis()
of = OpenFile()

f = "AU21_R2do6209_D78_Photocurrent.csv"
#f = "AU21_R2do6209_D78_PM.csv"

filename = "/Users/au/Desktop/Tyndall/Measurements/Caladan/Caladan20-21/EF-MIR2020/Run-2 do6209/do6209_QDL Coupon/AU-2-1/2022-01-19/" + f

#filename = of.get_signle_file()
df = pd.read_table(filename, sep=",")
col_name = df.columns

device_name = col_name[1:] # label for device on plot

x_max = 85
x = df[col_name[0]][:x_max]
ys = []
R=0.65
#print(len(x))

y_label_dict = {0:"WG Coupled Power (mW)", 1:"Total Power (mW)"}
x_label = df.columns[0]
y_label = y_label_dict[0]


y_i = []
line_label = device_name
def select_one_by_one():
    for label in device_name:

        #label = df.columns[i]
        y = df[label][:x_max]*1e3/R
        da.plot_XY(label, x_label, y_label, x, [y], plot_title="", range = (20, None), show_slope = False)
        #is_add = input("Add the device %s (y or n)"%i)

        ys.append(y)
        #y_i.append(i)
        #t = label.split("_")
        #t = sp.join(t[1:])
        ##sp = "-"
            #t=label.split("_")[1] # for cleaved facet 
            #t=label.split("_")
            #t = t[1] + t[3]

        #line_label.append(t)


select_one_by_one()

# print("Selected index")
# print(y_i)
plot_title = ""#"Etched Facet Facet"
legend_font = 10
label_fontsize = 14
da.plot_XYs(line_label,x_label, y_label, x, ys,plot_title=plot_title,legend_font=legend_font, label_fontsize=label_fontsize)


