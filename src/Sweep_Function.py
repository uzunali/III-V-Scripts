import time
from tkinter import filedialog, Tk


class IV_Sweep():
    """
        Implements the functionality for currnet or volateg sweep on channel A/B of the SMU.

        Args:
            initialize_connection: Initialize_GPIB() object 
            keithley_GPIB: Keithley GPIB command library (smu26xx)
            save_data: Write to csv file (Save_Data)
    """
    def __init__(self, initialize_connection, keithley_GPIB, save_data):
        self.initialize_connection = initialize_connection
        self.keithley_GPIB = keithley_GPIB
        self.save_data = save_data 
    
        
    def IV_sweep(self, filename, header, start_value, stop_value, step_size, voltage_limit = 3): 
        """
            Sweep current in channel A and measure volatage on the same channel.
    
        """

        self.keithley_GPIB.set_limit(channel= "a", unit="v", value=voltage_limit)
        
        unit = "mA"
        value_i = None
        
        self.save_data.save_to_csv_file(filename,header[:2], header_flag=True) # add the header for file    value = start_value
        value_i = start_value
        while value_i <= stop_value:
            
            self.keithley_GPIB.set_current_ChA(value_i*1e-3)
            #keithley_GPIB.set_voltage_ChA(value_i)
            
            self.keithley_GPIB.turn_ON_ChA()       
            time.sleep(0.5)
                
            #currenta = self.keithley_GPIB.get_current_ChA()
            voltageA = self.keithley_GPIB.get_voltage_ChA()
                   
            print("I=%s mA, V=%s V \n" %(value_i, voltageA))

                
            data = [value_i, voltageA]
            self.save_data.save_to_csv_file(filename, data, header_flag = False)
            value_i = value_i + step_size  
    
        self.keithley_GPIB.set_voltage_ChA(0)   
        self.keithley_GPIB.set_current_ChA(0) 
        #keithley_GPIB.set_voltage_ChB(0)  
        self.keithley_GPIB.turn_OFF_ChA()
        #terminate connection       
        self.initialize_connection.terminate_connection()
    
        # close the file
        self.save_data.close_file()
    
    def VI_sweep(self, filename, header, start_value, stop_value, step_size, current_limit = 100): 
        """
            Sweep current in channel A and measure volatage on the same channel.
    
        """
        unit = "V"
        value_i = None
        
        self.save_data.save_to_csv_file(filename,header[:2], header_flag=True) # add the header for file    value = start_value
        value_i = start_value
        while value_i <= stop_value:
            
            #self.keithley_GPIB.set_current_ChA(value_i)
            self.keithley_GPIB.set_voltage_ChA(value_i)
            
            self.keithley_GPIB.turn_ON_ChA()       
            time.sleep(0.5)
                
            #currenta = self.keithley_GPIB.get_current_ChA()
            currentA = self.keithley_GPIB.get_current_ChA()
                   
            print("I=%s mA, V=%s V \n" %(value_i, currentA))

                
            data = [value_i, currentA ]
            self.save_data.save_to_csv_file(filename, data, header_flag = False)
            value_i = value_i + step_size  
    
        self.keithley_GPIB.set_voltage_ChA(0)   
        self.keithley_GPIB.set_current_ChA(0) 
        #keithley_GPIB.set_voltage_ChB(0)  
        self.keithley_GPIB.turn_OFF_ChA()
        #terminate connection       
        self.initialize_connection.terminate_connection()
    
        # close the file
        self.save_data.close_file()
    
    
    def get_threshold(self, pre_power, cur_power):
        return cur_power/pre_power
    
    def LIV_sweep(self, filename, header, start_value, stop_value, step_size, voltage_limit = 3): 
        """
        Sweep current in channel A and measure volatage, get current reading from channel B 
        It could be photocurrent reading in which photodetector directly connected to Channel B of Keithley
        Or Analog Out of Power meter connedted to channel B of Keithley.

        header: [Current, Voltage, Power]
        start_value = (Integer) Current sweep start ie. 0 
        stop_value = (Iteger) Current sweep stop value ie. 100 for 100mA 
    
        """
        unit = "mA"
        value_i = None
        
        self.save_data.save_to_csv_file(filename,header, header_flag=True) # add the header for file
        value_i = start_value
        while value_i <= stop_value:
            
            # print("Set value is %f %s \n" % (value, unit))
            self.keithley_GPIB.set_current_ChA(value_i*1e-3)
            #keithley_GPIB.set_voltage_ChA(value_i)
            
            self.keithley_GPIB.turn_ON_ChA()       
            time.sleep(0.2)
                
            #currenta = self.keithley_GPIB.get_current_ChA()
            voltagea = self.keithley_GPIB.get_voltage_ChA()
    
            self.keithley_GPIB.turn_ON_ChB() 
            currentb = self.keithley_GPIB.get_current_ChB()
            #currentb = newport_PM.get_data()
                   
            print("I=%s mA, V=%s V, P=%s \n" %(value_i, voltagea, -currentb))    
        
            data = [value_i, voltagea,  -currentb ]
            self.save_data.save_to_csv_file(filename, data, header_flag = False)
            value_i = value_i + step_size      
        
        #print threshold
        # {k: v for k, v in sorted(threshold.items(),reverse=True, key=lambda item: item[1])}
    
        self.keithley_GPIB.set_voltage_ChA(0)   
        self.keithley_GPIB.set_current_ChA(0) 
    
        self.keithley_GPIB.set_voltage_ChB(0) 
        self.keithley_GPIB.set_current_ChB(0)  
    
        # turn OFF channels 
        self.keithley_GPIB.turn_OFF_ChA()       
        self.keithley_GPIB.turn_OFF_ChB()
        self.initialize_connection.terminate_connection()
        # close the file
        self.save_data.close_file()
    
    
    def do_test_sweep_IV(self, start_value, stop_value, step_size):
        """
        Do a test current sweep in channel A and measure volatage in channel A.
    
        """
        
        unit = "mA"
        value_i = start_value
        while value_i <= stop_value:
            
            #print("Set value is %f %s \n" % (value_i, unit))
            self.keithley_GPIB.set_current_ChA(value_i*1e-3)
            #keithley_GPIB.set_voltage_ChA(value_i)
            
            self.keithley_GPIB.turn_ON_ChA()       
            time.sleep(0.5)
                
            #currenta = self.keithley_GPIB.get_current_ChA()
            voltagea = self.keithley_GPIB.get_voltage_ChA()
                   
            print("I=%s %s, V=%s \n" %(value_i, unit, voltagea))
            
            #data = [value_i, voltagea, ]
            #save_data.save_to_csv_file(filename, data, header_flag = False)
            value_i = value_i + step_size    
    
        self.keithley_GPIB.set_voltage_ChA(0)   
        self.keithley_GPIB.set_current_ChA(0) 
        #keithley_GPIB.set_voltage_ChB(0)  
        self.keithley_GPIB.turn_OFF_ChA()       
        #keithley_GPIB.turn_OFF_ChB()
        #terminate connection
        self.initialize_connection.terminate_connection()