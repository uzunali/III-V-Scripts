import time
from src.Data_Analysis import Data_Analysis
#from Sweep_Function import IV_Sweep
from src.OpenFile import OpenFile
#from Newport_844_PE import Newport_844_PE

da = Data_Analysis()
of = OpenFile()


def plot_test():
    #da.plot_XmY()
    #da.plot_XmY_path("dat")
    #da.plot_XmY()
    #da.dR("dat", dI=1, n=10)
    da.Device_Analysis_v2()
    #pass

def test1():
    of.combine_into_signle_file()
    

def main():
    pass

if __name__ == "__main__":
    #main()
    #keithley_test()
    plot_test()
    #test_Newport()
    #test1()

