import time
from src.Keithley26xx_GPIB import smu26xx
from src.Initialize_Connection import Initialize_GPIB
from src.Data_Analysis import Data_Analysis
from src.Newport_844_PE import Newport_844_PE
from src.Sweep_Function import IV_Sweep
from src.OpenFile import OpenFile
from src.Thorlab_USBPM100D import Thorlab_100D


def list_device_GPIB():
    initialize_connection = Initialize_GPIB()
    print(initialize_connection.get_device_list())
    initialize_connection.terminate_connection()
    
    

def plot_test():
    da = Data_Analysis()
    da.plot_xy_multipleY()

def newport_USBPM_test():
    newport_PM = Newport_844_PE()
    for i in range(10):
        data = newport_PM.get_power_reading()
    print(type(data))
    newport_PM.close_connection()

def thorlab_PM100D_test():
    thorlab_PM = Thorlab_100D()
    # Open connection
    thorlab_PM.open_connection()
    
    
    # set wavelength
    wavelength = 1500
    thorlab_PM.set_wavelength(wavelength)
    
    # get power reading
    for i in range(0.3):
        data = thorlab_PM.get_power_reading()
        print(data)
    
        
        
    #close connection
    thorlab_PM.close_connection()

def keithley_function():
    initialize_connection = Initialize_GPIB()
    gpib_index = 0
    addr = 26 # change it if necessery
    inst = initialize_connection.connect_device(gpib_index, addr) # connect to device#

    # create an object
    keithley_GPIB =  smu26xx(inst)
    keithley_GPIB.set_limit("a", "v", 3)
    #keithley_GPIB.reset("b")
    
    
def get_current_In_ChB():
    initialize_connection = Initialize_GPIB()
    gpib_index = 0
    addr = 26 # change it if necessery
    inst = initialize_connection.connect_device(gpib_index, addr) # connect to device#

    # create an object
    keithley_GPIB =  smu26xx(inst)
    newport_PM = Newport_844_PE()
    
    data = newport_PM.get_power_reading()
    
    keithley_GPIB.turn_ON_ChB()
    
    
    for i in range(5):
        time.sleep(0.3)
        phI = keithley_GPIB.get_current_ChB()
        data = newport_PM.get_power_reading()
    
        print(data)
   
    keithley_GPIB.turn_OFF_ChB()
    newport_PM.close_connection()
    return()

def probe_alingmment_test():
    initialize_connection = Initialize_GPIB()
    gpib_index = 0
    addr = 26 # change it if necessery
    inst = initialize_connection.connect_device(gpib_index, addr) # connect to device#

    # create an object
    keithley_GPIB =  smu26xx(inst)
    
    # data = newport_PM.get_power_reading()
    
    keithley_GPIB.set_limit("a", "v", 3)
    keithley_GPIB.turn_ON_ChA()
    set_cur = 50
    keithley_GPIB.set_current_ChA(set_cur*1e-3)
    
    
    for i in range(200):
         time.sleep(0.3)
         data = keithley_GPIB.get_current_ChB()
    #     data = newport_PM.get_power_reading()
    
         print(data)
    #time.sleep(50)
    keithley_GPIB.turn_OFF_ChA()
    keithley_GPIB.turn_OFF_ChB()
    # newport_PM.close_connection()
    return()
    
    
    
    

def main():

    initialize_connection = Initialize_GPIB()
    #print(initialize_connection.get_device_list())

    gpib_index = 0
    addr = 26 # change it if necessery
    inst = initialize_connection.connect_device(gpib_index, addr) # connect to device#

    # create an object
    keithley_GPIB =  smu26xx(inst)
    save_data = OpenFile()
    
    newport_PM = Newport_844_PE()

    sweep_function = IV_Sweep(initialize_connection, keithley_GPIB, save_data, newport_PM)

    QDL_Coupon = True
    power_reading = ["Newport_PM", "Keithley_ChB"] #0 or 1
    power_index = 1 # 0 or 1
    
    #filename = "R2do6209_1.5mm_AF_RW_3.0um_T8.csv"
    #filename = "R2do6209_1pMIR_CL2mm_RW2.5um_MIRXumxXum_T1.csv"
    #filename = "AU21_R2do6209_S1D8_Photocurrent_R3.csv"
    
    #filename = "R2do6209_1mm_1pMIR_RW_5.0um_MIR_7.5x84um_Photocurrent.csv"
    #filename = "R2do6209_1.9mm_2pMIR_RW_2to5.0um_MIR_6.5x34um_Keithley_ChB.csv"
    #filename = "L-TT2-D1-R2do5960_1.5mm_1pMIR_RW_3um_MIR_6.5x52um_Keithley_ChB.csv"
  
  
      #do5960
    filename = "R1do6209_2mm_1pMIR_RW_Xum_MIR_Xum_D4_Photocurrent-r2.csv"
    #full_path = "\\\\fs1\\Docs2\\ali.uzun\\My Documents\\My Files\\Scripts\\Python\\III-V Scripts\\Data\\"
    measurement_base_path = "\\\\FS1\\Docs2\\ali.uzun\\My Documents\\My Files\\Measurements\\Caladan\\Caladan20-21\\EF-MIR2020\\"
    if (QDL_Coupon):
        save_to = "Run-2 do6209\\do6209 QDL Coupon\\do6209_QDL_on_60nm_PECVD SiO2\\2022-01-18\\"
        save_to = "Run-2 do6209\\do6209 QDL Coupon\\AU-2-1\\2022-02-28\\" 
        #save_to = "Run-2 do6209\\do6209 QDL Coupon\\QDL on Al2O3\\SOI3\\2022-02-09\\"
        
    else:
        #save_to = "Run-2 do6209\\do6209 QDL Coupon\\AU-2-1\\2022-01-07\\"
        device_list = {0:"Cleaved Facet Device", 1:"Etched Facet Device",2:"1pMIR Device",3:"2pMIR Device"}
        device_lemgth = {0:"CL1mm",1:"CL1.5mm",2:"CL2mm", 3:"CL1.9mm"}
        device_index = 2
        length_index = 2
        save_to = "Run-2 do6209\\do6209 FPL on GaAs\\Devices\\%s\\%s\\Detector Test\\" % (device_list[device_index],device_lemgth[length_index])
        save_to = "Run-1 do5960\\do5960 FPL on GaAs\\Devices\\%s\\%s\\" % (device_list[device_index],device_lemgth[length_index])
        
    
    print(save_to)
    full_path = measurement_base_path + save_to + filename

    # first column, second column, third column
    header = ["Current (mA)", "Voltage (V)", "Power (mA)"]

    start_value=0
    stop_value=80 #mA
    step_size=1 #mA
    
    
   #current_ranges = [1E-7, 1E-6, 1E-5, 1E-4, 1E-3, 1E-2, 1E-1, 1, 1.5]
    #keithley_GPIB.set_measurement_range("b","i",current_ranges[4])
    
    #sweep_function.IV_sweep(full_path, header, start_value=start_value, stop_value=stop_value, step_size=step_size)
    #plt.plot_IV(full_path)
    #sweep_function.IV_sweep(full_path, header, start_value, stop_value, step_size, voltage_limit = 3)
    
    if (power_reading[power_index] == "Newport_PM"):
        sweep_function.LIV_sweep_NewportPM(full_path, header, start_value=start_value, stop_value=stop_value, step_size=step_size, voltage_limit = 3)
    
    elif(power_reading[power_index] == "Keithley_ChB"):
        sweep_function.LIV_sweep_KeithleyChB(full_path, header, start_value=start_value, stop_value=stop_value, step_size=step_size, voltage_limit = 3)
    #sweep_function.do_test_sweep_IV(0, 60, 1)

if __name__ == "__main__":
    main()
    #list_device_GPIB()
    #probe_alingmment_test()
    #keithley_test() 
    #get_current_In_ChB  ()  
    #plot_test()
    #keithley_test()
    #newport_USBPM_test()
    #thorlab_PM100D_test()
    #get_current_In_ChB()
    #keithley_function()

