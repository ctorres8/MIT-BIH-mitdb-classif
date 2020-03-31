# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 17:02:56 2020

@author: crist
"""

import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt
import scipy.io as sio


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

ecg_ii = ECG['val'][0]
ecg_v5 = ECG['val'][1]
N_ecg_ii = len(ecg_ii)
N_ecg_v5 = len(ecg_v5)

fs = 360 #Hz

x1_ii = 40000 #muestra
x2_ii = 90000 #muestra

ii_w = ecg_ii[x1_ii:x2_ii]

Fxx_ii,Pxx_ii=sig.welch(ii_w,fs,window='hanning',nperseg=4096,noverlap=4096/2, nfft=4*4096)

#Calculo de la proporción de área
f_total = (Pxx_ii>0)
f_paso = (Fxx_ii>=0.13) & (Fxx_ii<=37)
area_total = np.trapz (Pxx_ii[f_total])
area_part = np.trapz (Pxx_ii[f_paso])
ratio_ii = (area_part/area_total)*100


plt.figure("Ventana Lead II")
plt.plot(ii_w, label='ecg lead II')

plt.title('Ventana Lead II')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [mV]')
plt.grid(which='both', axis='both')

axes_ecg_ii = plt.gca()
axes_ecg_ii.legend()

plt.figure("Densidad de potencia Lead II")
plt.plot(Fxx_ii,Pxx_ii,label ='DEP Lead II')
plt.title('DEP LEAD II')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [V^2]')
plt.grid(which='both', axis='both')
plt.xlim(-5,100,1)

plt.fill_between(Fxx_ii,Pxx_ii,color='orange',where=Fxx_ii>=0.13,label='area')
plt.fill_between(Fxx_ii,Pxx_ii,color='white',where=Fxx_ii>=37)

axes_DEP_II = plt.gca()
axes_DEP_II.legend()


# ****************************************************************************
# ****************************************************************************


x1_v5 = 3700 #muestra
x2_v5 = 11380 #muestra

v5_w = ecg_v5[x1_v5:x2_v5]

Fxx_v5,Pxx_v5=sig.welch(v5_w,fs,window='hanning',nperseg=4096,noverlap=4096/2, nfft=4*4096)

#Calculo de la proporción de área
f_total = (Pxx_v5>0)
f_paso = (Fxx_v5>=0.13) & (Fxx_v5<=38)
area_total = np.trapz (Pxx_v5[f_total])
area_part = np.trapz (Pxx_v5[f_paso])
ratio_v5 = (area_part/area_total)*100


plt.figure("Ventana Lead V5")
plt.plot(v5_w, label='ecg lead II')

plt.title('Ventana Lead V5')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [mV]')
plt.grid(which='both', axis='both')

axes_ecg_v5 = plt.gca()
axes_ecg_v5.legend()

plt.figure("Densidad de potencia Lead V5")
plt.plot(Fxx_v5,Pxx_v5,label ='DEP Lead V5')
plt.title('DEP LEAD II')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [V^2]')
plt.grid(which='both', axis='both')
plt.xlim(-5,100,1)

plt.fill_between(Fxx_v5,Pxx_v5,color='orange',where=Fxx_v5>=0.13,label='area')
plt.fill_between(Fxx_v5,Pxx_v5,color='white',where=Fxx_v5>=38)

axes_DEP_V5 = plt.gca()
axes_DEP_V5.legend()
