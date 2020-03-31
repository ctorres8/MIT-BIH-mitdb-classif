# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:20:52 2020

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
f_nyq = fs/2 # 180 Hz

    

## IIR

fs0=7
fp0=9
fp1=23
fs1=25

a_max =0.5
at = 40

bp_cheby = sig.iirdesign(wp=np.array([fp0,fp1])/f_nyq, ws=np.array([fs0,fs1])/f_nyq, gpass=a_max, gstop=at, analog=False, ftype='cheby1', output='sos')
ii_filtrada = sig.sosfiltfilt(bp_cheby,ecg_ii)
v5_filtrada = sig.sosfiltfilt(bp_cheby,ecg_v5)

EN_ii = pow(ii_filtrada,2)
EN_v5 = pow(v5_filtrada,2)


w=34
qrs_det_ii=[]
qrs_det_v5=[]

for i in range(0 , (N_ecg_ii-round(w/2))):
    if EN_ii[i]>6000 and EN_ii[i]==max(EN_ii[i-round(w/2):i+round(w/2)]):
        qrs_det_ii.append(int(np.where(EN_ii == EN_ii[i])[0]))  


for i in range(0 , (N_ecg_v5-round(w/2))):
    if EN_v5[i]>620 and EN_v5[i]==max(EN_v5[i-round(w/2):i+round(w/2)]):
        qrs_det_v5.append(int(np.where(EN_v5 == EN_v5[i])[0]))
        


plt.figure("Detección del complejo QRS ")
plt.plot(ecg_ii,label='ecg lead II')
#plt.plot(v5_filtrada,label='V5 Filtrda')
plt.plot(ii_filtrada,label='MLII Filtrda')
#plt.plot(qrs_det,ecg_ii[qrs_det],'x', label='detecciones de latidos')
#plt.plot(ecg_v5,label='ecg lead II')
#plt.plot(qrs_det_v5,ecg_v5[qrs_det_v5],'x', label='detecciones de latidos')
#plt.plot(EN_ii, label='Energía BPF MLII')
#plt.plot(qrs_det_ii,EN_v5[qrs_det_ii],'x',label='Detecciones de latidos')
#plt.plot(EN_v5, label='Energía BPF V5')
#plt.plot(qrs_det_v5,EN_v5[qrs_det_v5],'x',label='Detecciones de latidos')


plt.title('Detecciones de latidos')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [mV^2]')
plt.grid(which='both', axis='both')

axes_ecg_ii = plt.gca()
axes_ecg_ii.legend()

