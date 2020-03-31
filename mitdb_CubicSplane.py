# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:10:27 2020

@author: crist
"""

import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.interpolate import CubicSpline 


ECG = sio.loadmat('100m.mat')

"""

100m 2 360 650000
100m.mat 16+192 200/mV 11 0 -29 27021 0 MLII
100m.mat 16+192 200/mV 11 0 -13 3668 0 V5
# 69 M 1085 1629 x1
# Aldomet, Inderal
#Creator: wfdb2mat
#Source: record mitdb/100

"""

ecg_ii = ECG['val'][0]#[250:]#649940]
ecg_v5 = ECG['val'][1]#[250:649940]
N_ecg_ii = len(ecg_ii)
N_ecg_v5 = len(ecg_v5)


fs = 360 #Hz
f_nyq = fs/2 # 180 Hz

######### IIR

fs0=7
fp0=9
fp1=23
fs1=25

a_max =0.5
at = 40

bp_cheby = sig.iirdesign(wp=np.array([fp0,fp1])/f_nyq, ws=np.array([fs0,fs1])/f_nyq, gpass=a_max, gstop=at, analog=False, ftype='cheby1', output='sos')
ii_filtrada = sig.sosfiltfilt(bp_cheby,ecg_ii)
v5_filtrada = sig.sosfiltfilt(bp_cheby,ecg_v5)
####################################################


EN_ii = pow(ii_filtrada,2) #Elevo al cuadrado para tener la energia del ML II y que sea más facil detectar el QRS
EN_v5 = pow(v5_filtrada,2)

############### Deteccion de latidos
w=34

## PARA ML II
qrs_det_ii=[]

for i in range(0 , (N_ecg_ii-round(w/2))):
    if EN_ii[i]>6000 and EN_ii[i]==max(EN_ii[i-round(w/2):i+round(w/2)]):
        qrs_det_ii.append(int(np.where(EN_ii == EN_ii[i])[0]))  

qrs_det_ii.append(649991 )


## PARA V5
qrs_det_v5=[]

for i in range(0 , (N_ecg_v5-round(w/2))):
    if EN_v5[i]>620 and EN_v5[i]==max(EN_v5[i-round(w/2):i+round(w/2)]):
        qrs_det_v5.append(int(np.where(EN_v5 == EN_v5[i])[0]))
        
        
N_QRS_II = len(qrs_det_ii)
N_QRS_V5 = len(qrs_det_v5)        
#######################################


############## INTERPOLACION POR CUBIC SPLANE
##PARA LA DERIVACION ML II

x_ii = np.arange(N_QRS_II)
pq_ii=[]
for i in range(0,N_QRS_II-1):
    pq_ii.append(qrs_det_ii[i]-30)
y_ii=ecg_ii[pq_ii]
cs_ii = CubicSpline(pq_ii,y_ii)
xs_ii = np.arange(0,N_ecg_ii,1)

salida_ii = ecg_ii - cs_ii(xs_ii)

## PARA LA DERIVACION V5

x_v5 = np.arange(N_QRS_V5)
pq_v5=[]
for i in range(0,N_QRS_V5-1):
    pq_v5.append(qrs_det_v5[i]-30)
y_v5=ecg_v5[pq_v5]
cs_v5 = CubicSpline(pq_v5,y_v5)
xs_v5 = np.arange(0,N_ecg_v5,1)

salida_v5 = ecg_v5 - cs_v5(xs_v5)

############################################################
"""
sio.savemat('ECG.mat',{'MLII':salida_ii,'V5':salida_v5,'QRS_DET_II':qrs_det_ii,'QRS_DET_V5':qrs_det_v5}) # Creo un archivo .mat para extraer las variables

plt.figure("Interpolación mediante Cubic Spline ")
#plt.plot(ecg_ii,label ='ecg lead')
#plt.plot(salida_ii, label='salida')
plt.plot(ecg_v5,label ='ecg lead')
plt.plot(salida_v5, label='salida')

#plt.plot(x,pq[x],label="data")
#plt.plot(pq,y,label="data")
#plt.plot(xs,cs(xs),'orange',label="cubic splane")
#plt.plot(xs,cs(xs,1),label="cubic splane")
#plt.plot(ecg_lead,label ='ecg lead')
#plt.plot(qrs_det[x],ecg_lead[qrs_det[x]],'x', label='deteccion de latidos')
#plt.plot(pq[x],ecg_lead[pq[x]],'x',label='segmento PQ')
plt.title('Interpolación mediante Cubic Spline')
plt.xlabel('Muestras')
plt.ylabel('Amplitud ')
plt.grid(which='both', axis='both')

axes_hdl_CS = plt.gca()
axes_hdl_CS.legend()
"""