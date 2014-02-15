# functions to calculation the mean value of each basin in each year
import glob 
from pyhdf.SD import SD, SDC
import numpy as np

def trmm_mean_nz(year):
    file = glob.glob('/Users/yuewang/Documents/DATA/atl/ATL_3B42V7_rain_accum.'+ str(year)+'*')

    rainfall_0 = []
    for i in file:
        atl =SD(i,SDC.READ)
        rainfall = atl.select('RAIN_TOTAL')
        rainfall_value = rainfall.get()
        rainfall_0.append(rainfall_value)

        rainfall_single = np.array(rainfall_0)
        rainfall_annual = sum(rainfall_single)
  
    ind = np.where(rainfall_annual != 0)
    rf_annual = []
    for i,j in zip(*ind):
        mm = rainfall_annual[i,j]
        rf_annual.append(mm)
    rf_annual = np.array(rf_annual)

    
    a = np.mean(rf_annual)
    return a


def trmm_mean(year):
    file = glob.glob('/Users/yuewang/Documents/DATA/atl/ATL_3B42V7_rain_accum.'+ str(year)+'*')

    rainfall_0 = []
    for i in file:
        atl =SD(i,SDC.READ)
        rainfall = atl.select('RAIN_TOTAL')
        rainfall_value = rainfall.get()
        rainfall_0.append(rainfall_value)

    rainfall_single = np.array(rainfall_0)
    rainfall_annual = sum(rainfall_single)

#    nonzone = np.where(rainfall_annual != 0)
    b = np.mean(rainfall_annual)
    return b
    
def rainfall_anunal_GMX(year):

    file = glob.glob('/Users/yuewang/Documents/DATA/atl/ATL_3B42V7_rain_accum.'+ str(year)+'*')

    rainfall_0 = []
    for i in file:
        atl =SD(i,SDC.READ)
        rainfall = atl.select('RAIN_TOTAL')
        rainfall_value = rainfall.get()
        rainfall_0.append(rainfall_value)
    
    rainfall_single = np.array(rainfall_0)
    rainfall_anunal = sum(rainfall_single)
    rainfall_anunal_GMX = rainfall_anunal[280:320,340:400]
    
    ind = np.where(rainfall_anunal_GMX != 0)
    rf_annual = []
    for i,j in zip(*ind):
        mm = rainfall_anunal_GMX[i,j]
        rf_annual.append(mm)
    rf_annual = np.array(rf_annual)
    
    c = np.mean(rf_annual)
    
    return c

def rainfall_anunal_car(year):

    file = glob.glob('/Users/yuewang/Documents/DATA/atl/ATL_3B42V7_rain_accum.'+ str(year)+'*')

    rainfall_0 = []
    for i in file:
        atl =SD(i,SDC.READ)
        rainfall = atl.select('RAIN_TOTAL')
        rainfall_value = rainfall.get()
        rainfall_0.append(rainfall_value)
    
    rainfall_single = np.array(rainfall_0)
    rainfall_anunal = sum(rainfall_single)
    rainfall_anunal_car = rainfall_anunal[238:286,372:476]
    
# calculation none-zone mean value    
    ind = np.where(rainfall_anunal_car != 0)
    rf_annual = []
    for i,j in zip(*ind):
        mm = rainfall_anunal_car[i,j]
        rf_annual.append(mm)
    rf_annual = np.array(rf_annual)
    
    d = np.mean(rf_annual)
    
    return d
    
def rainfall_anunal_eco(year):

    file = glob.glob('/Users/yuewang/Documents/DATA/atl/ATL_3B42V7_rain_accum.'+ str(year)+'*')

    rainfall_0 = []
    for i in file:
        atl =SD(i,SDC.READ)
        rainfall = atl.select('RAIN_TOTAL')
        rainfall_value = rainfall.get()
        rainfall_0.append(rainfall_value)
    
    rainfall_single = np.array(rainfall_0)
    rainfall_anunal = sum(rainfall_single)
    rainfall_anunal_eco = rainfall_anunal[286:360,400:520]
    
    ind = np.where(rainfall_anunal_eco != 0)
    rf_annual = []
    for i,j in zip(*ind):
        mm = rainfall_anunal_eco[i,j]
        rf_annual.append(mm)
    rf_annual = np.array(rf_annual)
    
    e = np.mean(rf_annual)
    
    return e




    
    

