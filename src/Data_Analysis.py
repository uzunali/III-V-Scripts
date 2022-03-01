#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:37:50 2021

@author: aliuzun
"""
import csv, random
import os
from tkinter import Label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from OpenFile import OpenFile

fl = OpenFile()

class Data_Analysis():
    def __init__(self):
        self.line_style = ["solid","dotted","dashed","dashdot"]
 

    def get_differantial_Resistance(self, I, V, dI):
        Rd = []
        #dt = 2
        for s in range(len(I)-dI):
            try:
                dv = (V[dI]-V[s])
                di = (I[dI]-I[s])
                rt = dv/di
                Rd.append(rt*1e3)
                dI = dI + 1
            except(KeyError):
                print(dI)
        return(Rd)

    def dR(self,file_type, dI,n):
        """
        dt differential step
        """
        filename = fl.get_signle_file()
        labels = {"Voltage":" (V)", "Current":" (mA)","Differential Resistance":" (Ohm)"}

        if(file_type == "csv"):
            I,V,P = fl.read_csv_file(filename)
        else:
            I,V,P = fl.read_dat_file(filename)
        dR = self.get_differantial_Resistance(I, V, dI)
        x_length = len(I)  
        try: 
            dR.extend((x_length-len(dR))*[None])
            dR[0:n] = [None]*n
        except AttributeError: pass

        #V = df[col_name[1]]
        
        x_label = I.name + labels[I.name]
        y_label1 = V.name + labels[V.name]
        y_label2 = "Differential Resistance (Ohm)"

        self.plot_yxy(I, V, dR, x_label, y_label1, y_label2)


    def get_slope(self, x, y, range=(0,None)):
        """
        return the slope of line for given interval
        ie. slope efficiency and resistance
        """
        start,end = range
        if (end != None):
            x = x[start:end]
            y = y[start:end]
        m, b = np.polyfit(x[start:], y[start:], 1) # m = slope, b = intercept
        return (m,b)
    
    def plot_XY(self, device_name, x_label, y_label, x, y, plot_title, range = (20, None), show_slope = False):
        """
            Return XY plor for given x,y pair. 
            Labels: Voltage versus Power or Current
        """
        labels = {"Voltage":" (V)", "Current":" (mA)","Power":" (mW)"}
        plot_text = {"Voltage":"R:%f Ohm", "Power":"Slope Efficiency: %f W/A"}
        #x_label = x.name + labels[x.name]
        #y_label = y.name + labels[y.name]

        t=0
        if (t):
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.plot(x, y, linewidth=4)
            if (show_slope):
                slope, c = self.get_slope(x,y,range)
                plt.plot(x, slope*x+ c,'--',Label=device_name)
                #if(y.name == "Voltage"):
                #    slope = slope*1e3
                plt.text(x[20], y[100], "Slope is %f"%(slope))
            plt.title(plot_title)
            plt.grid(True)
            plt.show()
        else:
            plot_title = ""
            device_name = [device_name]
            self.plot_XYs(device_name, x_label, y_label, x, y, plot_title = plot_title, legend_font=10, legend_position=0, label_fontsize=18,axis_value_fontsize=14, lwidth = 2)

    def plot_yxy(self, x, y1, y2, x_label, y_label1, y_label2):
        """
            Plot in y |___| y1 format
                        x 
            Labels: Voltage versus Power or Current
        """
        labels = {"Voltage":" (V)", "Current":" (mA)","Power":" (mW)"}
        # plot_text = {"Voltage":"R:%f Ohm", "Power":"Slope Efficiency: %f W/A"}
        # x_label = x.name + labels[x.name]
        # y_label1 = y1.name + labels[y1.name]
        # y_label2 = y2.name + labels[y2.name]
        # create figure and axis objects with subplots()
        fig,ax = plt.subplots()
        plt.grid(True)
        # make a plot
        ax.plot(x, y1, color="red")
        # set x-axis label
        ax.set_xlabel(x_label, fontsize=14)
        # set y-axis label
        ax.set_ylabel(y_label1, color="red", fontsize=14)

        # twin object for two different y-axis on the sample plot
        ax2=ax.twinx()
        # make a plot with different y-axis using second axis object
        ax2.plot(x, y2, color="blue")
        ax2.set_ylabel(y_label2, color="blue", fontsize=14)
        plt.show()
        #save_plot(fig)

    def plot_XYs(self, device_name, x_label, y_label, x, ys, plot_title = "Plot Title", legend_font=8, legend_position=0, label_fontsize=10,axis_value_fontsize=14, lwidth = 2):
        """
        Plot x vs multiple y 

        legend position key:
        'best'            0
        'upper right'     1
        'upper left'      2
        'lower left'      3
        'lower right'     4
        'right'           5
        'center left'     6
        'center right'    7
        'lower center'    8
        'upper center'    9
        'center'          10
        """
        plt.xlabel(x_label,fontsize=label_fontsize)
        plt.ylabel(y_label,fontsize=label_fontsize)

        #plt.plot(x, ys[0], linewidth=2)
        x_length = len(x)

        for i,y in enumerate(ys):
            line_type = random.randint(0,len(self.line_style)-1)
            try: y.extend((x_length-len(y))*[None])
            except AttributeError: pass
            plt.plot(x, y, linewidth=lwidth,linestyle = self.line_style[line_type], label=device_name[i])
        plt.title(plot_title)
        plt.xticks(fontsize=axis_value_fontsize)
        plt.yticks(fontsize=axis_value_fontsize)
        plt.legend(fontsize=legend_font,loc=legend_position)
        plt.grid(True)
        plt.show()

    def plot_XmY(self, y_scale=1, is_LI = True, plot_title = "Plot Title", legend_font=8, legend_position=0, label_fontsize=10,axis_value_fontsize=14, lwidth = 2):
        """
            Open a file and plots X vs Y1 ....Y2 for selected file
            Labels: Voltage versus Power or Current
        """
        filename = fl.get_signle_file()
        labels = {"Voltage":" (V)", "Current":" (mA)","Power":" (mW)"}
        plot_text = {"Voltage":"R:%f Ohm", "Power":"Slope Efficiency: %f W/A"}

        df = pd.read_csv (filename)
        col_name = df.columns
        x = df[col_name[0]]
        device_name = col_name[1:] # label for device on plot
        try:
            x_label = x.name + labels[x.name]
        except:
            x_label = x.name
        plot_title = "IV Plot"
        y_label = "Voltage (V)"
        #plot_title%("IV")
        if (is_LI):
            y_label = "Power mW)"
            plot_title = "LI Plot"
            #plot_title%("LI")
      
        ys = []
        for i in range(len(col_name)-1):
            ys.append(df[col_name[i+1]]*y_scale)

        self.plot_XYs(device_name, x_label, y_label, x, ys, plot_title = plot_title, legend_font=legend_font, legend_position=legend_position,label_fontsize=label_fontsize,axis_value_fontsize=axis_value_fontsize, lwidth = lwidth)
    

    def plot_XmY_path(self, file_type):
        """
            Open files at selected path and plots X vs Y1 ....Y2
            Labels: Voltage versus Power or Current
            file_type: "csv" or "dat"
        """
        x_label = "Current (mA)"

        filepath = fl.get_files_path()
        file_list = fl.get_file_list(filepath, file_type)
        device_name = [] # devicel label on plot
             
        X = []
        Vs = []
        Ps =[]
        try:
            for filename in file_list:
                fn = filename.split("/")[-1].split(".")[0]
                #fn ="_".join(fn.split("_")[2:])
                device_name.append(fn)
                if(file_type == "csv"):
                    I,V,P = fl.read_csv_file(filename)
                else:
                    I,V,P = fl.read_dat_file(filename)
                if (len(I)> len(X)):
                    X = I.tolist()
                Vs.append(V.tolist())
                try: Ps.append(P.tolist())
                except(AttributeError):
                    pass
        except ValueError:
            print(fn)

        y_label = "Power mW)"
        self.plot_XYs(device_name,x_label,y_label,X,Ps, plot_title = None)

        y_label = "Voltage (V)"
        self.plot_XYs(device_name,x_label,y_label,X,Vs,plot_title = None)

    #def plot_XmY_path2(self):
    #------------------------------
    def Device_Analysis(self, file_type):
        """
            Open files at selected path and for each device you could calculate/get
            1) Threshold current
            2) Slope efficiency
            3) Differential Resistance

            file_type: "csv" or "dat"
        """
        x_label = "Current (mA)"

        filepath = fl.get_files_path()
        file_list = fl.get_file_list(filepath, file_type)
        device_name = [] # devicel label on plot
             
        X = []
        Vs = []
        Ps =[]
        try:
            for filename in file_list:
                fn = filename.split("/")[-1].split(".")[0]
                #fn ="_".join(fn.split("_")[2:])
                device_name.append(fn)
                if(file_type == "csv"):
                    I,V,P = fl.read_csv_file(filename)
                else:
                    I,V,P = fl.read_dat_file(filename)
                if (len(I)> len(X)):
                    X = I.tolist()
                Vs.append(V.tolist())
                try: Ps.append(P.tolist())
                except(AttributeError):
                    pass
        except ValueError:
            print(fn)

        y_label = "Power mW)"
        self.plot_XYs(device_name,x_label,y_label,X,Ps, plot_title = None)

        y_label = "Voltage (V)"
        self.plot_XYs(device_name,x_label,y_label,X,Vs,plot_title = None)



    def Device_Analysis_v2(self, is_LI = True):
        """
            Open selected file and for each device you could calculate/get
            1) Threshold current
            2) Slope efficiency
            3) Differential Resistance

            Labels: Voltage versus Power or Current
        """
        filename = fl.get_signle_file()
        labels = {"Voltage":" (V)", "Current":" (mA)","Power":" (mW)"}
        plot_text = {"Voltage":"R:%f Ohm", "Power":"Slope Efficiency: %f W/A"}

        df = pd.read_csv(filename)
        col_name = df.columns
        x = df[col_name[0]]
        device_name = col_name[1:] # label for device on plot
        x_label = x.name + labels[x.name]
        plot_title = "IV Plot"
        y_label = "Voltage (V)"
        #plot_title%("IV")
        if (is_LI):
            y_label = "Optical Power (mW)"
            plot_title = "LI Plot"
            #plot_title%("LI")
    
        ys = []
        for i in range(len(col_name)-1):
            y = df[col_name[i+1]]
            dev_label = col_name[i+1]
            
            self.plot_XY(x_label, y_label, x, y, dev_label,range = (20, None), show_slope = False)
            slope_range = input("Enter the range start and end: (i.e 25, 100) ")
            range_start = int(slope_range.split(",")[0])
            range_end = int(slope_range.split(",")[1])
            self.plot_XY(x_label, y_label, x, y, dev_label,range = (range_start, range_end), show_slope = True)
            repeat = input("Repeat the plot!!! (y or n)")

            if (repeat=="y"):
                range_start = int(slope_range.split(",")[0])
                range_end = int(slope_range.split(",")[1])
                self.plot_XY(x_label, y_label, x, y, dev_label,range = (range_start, range_end), show_slope = True)


            ys.append(y)
    
    #------------------------------

    def nice_plut(self): # MIR analysis
        plt.plot([1,2],[3,5],'ro',label='one')
        plt.plot([1,2],[1,2],'g^',label='two')
        plt.plot([1,2],[1,6],'bs',label='three')
        plt.axis([0,4,0,10])
        plt.ylabel('x2')
        plt.xlabel('x1')
        plt.legend()
        plt.show()

    def plot_LIV(self,x,y1,y2):
        # create figure and axis objects with subplots()
        fig,ax = plt.subplots()
        plt.grid(True)
        # make a plot
        ax.plot(x, y1, color="red")
        # set x-axis label
        ax.set_xlabel('Current (mA)', fontsize=14)
        # set y-axis label
        ax.set_ylabel("Voltage (V)", color="red", fontsize=14)

        # twin object for two different y-axis on the sample plot
        ax2=ax.twinx()
        # make a plot with different y-axis using second axis object
        ax2.plot(x, y2, color="blue")
        ax2.set_ylabel("Power (mW)", color="blue", fontsize=14)
        plt.show()
        #save_plot(fig)

    def save_plot(self,fig):
        # save the plot as a file
        fig.savefig('/Data/LIV.jpg',
                    format='jpeg',
                    dpi=300,
                bbox_inches='tight')
