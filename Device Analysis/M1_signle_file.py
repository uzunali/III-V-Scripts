import sys
sys.path.append("/Users/au/Desktop/Tyndall/Scripts/Python/III-V Scripts/src")

import pandas as pd
import csv
from itertools import zip_longest
from OpenFile import OpenFile

fl = OpenFile()

#filepath ='/Users/au/Desktop/Tyndall/Measurements/Caladan/Caladan20-21/EF-MIR2020/Run-2 do6209/do6209_FBL on GaAs/Devices/Cleaved Facet Device/CL1mm/LIV/' #R2do6209_1mm_1pMIR_RW_2.5um_MIR_6x48um_Photocurrent.csv
filepath = fl.get_files_path()
file_list = fl.get_file_list(filepath, file_type="csv")

# dictionary of lists 
device_label_IV = {}
device_label_LI = {}
row_number = 0  

R = 0.65
filename_become_col_name = True

for ffn in file_list:
    
    if (not filename_become_col_name):
        fl = ffn.split("/")[-1].strip(".csv").split("_")
        sp = "-"
        fl = sp.join(fl[1:3])
    else:
        fl = ffn.split("/")[-1]

    
    #print(fl)


    df = pd.read_csv(ffn)
    #col_names = ['Current', 'Power', 'Voltage']
    if(len(df.columns)==2):
        #df.columns = ['Current', 'Voltage']
        pass
    else:
        df.columns = ['Current', 'Voltage', 'Power']
    try:
    # list of columns
        I = df["Current"]
        V = df["Voltage"]
        P = df["Power"]/R

        # add Current column 
        device_label_LI.setdefault("Current (mA)",I)
        device_label_IV.setdefault("Current (mA)",I)
        
        if(len(I) > row_number):
            #print("New I %f, old I %f "%(len(I),row_number))
            I = df["Current"]
            row_number = len(I)
            device_label_LI.update({"Current (mA)":I})
            device_label_IV.update({"Current (mA)":I})
            
        

        if (fl in device_label_LI):
            fl = fl + "-1"
        device_label_LI.setdefault(fl,P)
        device_label_IV.setdefault(fl,V)
    except:
        print("File does not have correct column")
        pass
print(len(device_label_LI["Current (mA)"]))  
df_LI = pd.DataFrame(device_label_LI)
df_IV = pd.DataFrame(device_label_IV)

# saving the dataframe
file_name = "do6209_QDL_on_40nm-AL2O3_on SOI3_%s.csv"
df_LI.to_csv(filepath + file_name%"LI", header=True, index=False)
df_IV.to_csv(filepath + file_name%"VI", header=True, index=False)