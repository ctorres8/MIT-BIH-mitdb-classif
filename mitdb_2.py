# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:58:53 2020

@author: crist
"""

import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt
import scipy.io as sio


ECG = sio.loadmat('100m.mat')

ECG_CLEAN = sio.loadmat('ECG.mat')

ecg_ii = ECG['val'][0]
ecg_v5 = ECG['val'][1]

mlii = ECG_CLEAN['MLII'][0]
v5 = ECG_CLEAN['V5'][0]
qrs_ii = ECG_CLEAN['QRS_DET_II'][0]
qrs_v5 = ECG_CLEAN['QRS_DET_V5'][0]

N_MLII = len(mlii)
N_V5 = len(v5)
N_QRS_II = len(qrs_ii)-2
N_QRS_V5 = len(qrs_v5)-2

## MATRIZ DE LATIDOS
latidos_ii=[None]*(N_QRS_II-1)
for i in range(N_QRS_II-1):
    latidos_ii[i]=[None]*270

for j in range(1,N_QRS_II):
    latidos_ii[j-1]=mlii[(qrs_ii[j]-100):(qrs_ii[j]+170)]

    
latidos_v5=[None]*(N_QRS_V5-1)
for i in range(N_QRS_V5-1):
    latidos_v5[i]=[None]*270

for j in range(1,N_QRS_V5):
    latidos_v5[j-1]=v5[(qrs_v5[j]-100):(qrs_v5[j]+170)]
##################################

"""
## PROMEDIO DE LATIDOS
latidos_prom_ii=[0]*270
for i in range (0,len(latidos_ii)):
    latidos_prom_ii=latidos_prom_ii+latidos_ii[i]

latidos_prom_ii=latidos_prom_ii/len(latidos_ii)

latidos_prom_v5=[0]*270
for i in range (0,len(latidos_v5)):
    latidos_prom_v5=latidos_prom_v5+latidos_v5[i]

latidos_prom_v5=latidos_prom_v5/len(latidos_v5)

plt.figure("Latido Promedio V5")
plt.plot(latidos_prom_v5,label='latido promedio V5')
plt.title('Promedios de latidos de la derivación V5')
plt.xlabel('Tiempo[ms]')
plt.ylabel('Amplitud ')
plt.grid(which='both', axis='both')

axes_LAT_PROM_V5 = plt.gca()
axes_LAT_PROM_V5.legend()

plt.figure("Latido Promedio MLII")
plt.plot(latidos_prom_ii,label='Latido promedio MLII')
plt.title('Promedios de latidos de la derivación MLII')
plt.xlabel('Tiempo[ms]')
plt.ylabel('Amplitud ')
plt.grid(which='both', axis='both')

axes_LAT_PROM_II = plt.gca()
axes_LAT_PROM_II.legend()

######################################3

"""
### PARAMETROS R Y T

param_R_ii = []
param_T_ii = []
#param_W_ii = []

for i in range(0,N_QRS_II-1):
    param_R_ii.append(max(latidos_ii[i]))
    param_T_ii.append(latidos_ii[i][220] )
    
matrix_lat_ii =[range(2) for i in range(N_QRS_II)]

for i in range(N_QRS_II-1):
    matrix_lat_ii[i] = param_R_ii[i],param_T_ii[i]



param_R_v5 = []
param_T_v5 = []
#param_W_V5 = []

for i in range(0,N_QRS_V5-1):
    param_R_v5.append(max(latidos_v5[i]))
    param_T_v5.append(latidos_v5[i][220] )
    
matrix_lat_v5 =[range(2) for i in range(N_QRS_V5)]

for i in range(N_QRS_V5-1):
    matrix_lat_v5[i] = param_R_v5[i],param_T_v5[i]
    
    
    

plt.figure("parametros RTW V5")
#plt.plot(param_R_v5,'.',label='amplitud R')
#plt.plot(param_T_v5,'.',label='onda T')
plt.plot(param_R_v5, param_T_v5,'.',label='T=f(R)')
plt.title('Parametros R y T en la derivación V5')
plt.xlabel('Parametro R')
plt.ylabel('Parametro T ')
plt.grid(which='both', axis='both')

axes_RT_V5 = plt.gca()
axes_RT_V5.legend()

plt.figure("parametros RTW MLII")
#plt.plot(param_R_ii,'.',label='amplitud R')
#plt.plot(param_T_ii,'.',label='onda T')
plt.plot(param_R_ii, param_T_ii,'.',label='T=f(R)')
plt.title('Parametros R y T en la derivación MLII')
plt.xlabel('Parametro R')
plt.ylabel('Parametro T ')
plt.grid(which='both', axis='both')

axes_RT_MLII = plt.gca()
axes_RT_MLII.legend()


#################################################################

"""
plt.figure("Latidos Agrupados V5")
for i in range(1,len(latidos_v5)):
    plt.plot(latidos_v5[i],'blue')
plt.title('Latidos Agrupados V5')
plt.xlabel('Tiempo[ms]')
plt.ylabel('Amplitud ')
plt.grid(which='both', axis='both')

#axes_hdl_LAT_V5 = plt.gca()
#axes_hdl_LAT_V5.legend()


plt.figure("Latidos Agrupados MLII")
for i in range(1,len(latidos_ii)):
    plt.plot(latidos_ii[i],'blue')
plt.title('Latidos Agrupados MLII')
plt.xlabel('Tiempo[ms]')
plt.ylabel('Amplitud ')
plt.grid(which='both', axis='both')

axes_hdl_LAT_II = plt.gca()
axes_hdl_LAT_II.legend()
"""

"""
plt.figure("ECG LEAD MLII")
#plt.plot(ecg_ii, label='lead II')
#plt.plot(qrs_det,ecg_ii[qrs_det],'x', label='detecciones de latidos')
plt.plot(mlii,label='lead II interpolada')

plt.title('ECG LEAD II')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [mV]')
plt.grid(which='both', axis='both')

axes_ecg_ii = plt.gca()
axes_ecg_ii.legend()
"""