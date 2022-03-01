import sys
sys.path.append("/Users/au/Desktop/Tyndall/Scripts/Python/III-V Scripts/src")

from OpenFile import OpenFile
from Data_Analysis import Data_Analysis
import pandas as pd

da = Data_Analysis()
of = OpenFile()



#f = "AU21_R2do6209_D78_PM.csv"
device_list = {0:"Cleaved Facet Device",1:"Etched Facet Device",2:"1pMIR Device",3:"2pMIR Device",4:"Tapered Laser Device"}
CL_list = {1:"CL1mm",1:"CL1.5mm",2:"CL2mm"}

base_path = "/Users/au/Desktop/Tyndall/Measurements/Caladan/Caladan20-21/EF-MIR2020/"

cl = ["2.5","3.0","3.5"]
mtype = ["Newport_Keithley_ChB","Keithley_ChB_PM","Newport_PM"]

# dictionary of lists 
device_label_IV = {}
device_label_LI = {}
row_number = 0  

cl_index = 2

for i in range(3):
    fl = "%s"%(mtype[i])
    f = "R2do6209_2mm_EF_RW_%sum_%s.dat" % (cl[cl_index],mtype[i])
    device_path = "Run-2 do6209/do6209_FBL on GaAs/Devices/%s/%s/Detector Test/%s"%(device_list[0],CL_list[2],f)
    full_filename = base_path + device_path
    #print(full_filename)

    df = pd.read_table(full_filename, sep=",")
    #print(mtype[0])
    print(f)
    print(df.columns)
    
    try:
        
        I = df["Current (mA)"]
        V = df["Voltage (V)"]
        P = df["Power (mA)"]
    except:
        #df.columns = ['Current (mA)', 'Power (mA)','Voltage (V)' ]
        # I = df.iloc[:, 0]
        # V = df.iloc[:, 2]
        # P = df.iloc[:, 1]
        print("NNN")

    #print(len(I))

    if(len(I) > row_number):
            I = df["Current (mA)"]
            row_number = len(I)
            device_label_LI.setdefault("Current (mA)",I)
            device_label_IV.setdefault("Current (mA)",I)
    device_label_LI.setdefault(fl,P)
    device_label_IV.setdefault(fl,V)

df_LI = pd.DataFrame(device_label_LI)
df_IV = pd.DataFrame(device_label_IV)

# saving the dataframe
save_to_file = True
if (save_to_file):
    out_filename = "Detector Check Cleaved Facet %sum LI.csv" % cl[cl_index]
    save_to = "Device Analysis/Data/" + out_filename
    df_LI.to_csv(save_to, header=True, index=False)

    out_filename = "Detector Check Cleaved Facet %sum VI.csv" % cl[cl_index]
    save_to = "Device Analysis/Data/" + out_filename
    df_IV.to_csv(save_to, header=True, index=False)
