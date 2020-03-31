# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:29:10 2020

@author: crist
"""

import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt
import scipy.io as sio


ECG = sio.loadmat('100m.mat')

ECG_MLII = sio.loadmat('ECG_MLII.mat')


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

fs0=0.1
fp0=0.2
fp1=37
fs1=38

a_max =0.5
at = 20

bp_cheby = sig.iirdesign(wp=np.array([fp0,fp1])/f_nyq, ws=np.array([fs0,fs1])/f_nyq, gpass=a_max, gstop=at, analog=False, ftype='cheby1', output='sos')
ECG_cheby_ii = sig.sosfiltfilt(bp_cheby,ecg_ii)
ECG_cheby_v5 = sig.sosfiltfilt(bp_cheby,ecg_v5)

"""
med = sig.medfilt(ecg_ii,kernel_size=200-1)

b = sig.medfilt(med,kernel_size=600-1)

x = ecg_ii - b

bp_cheby = sig.iirdesign(wp=36/f_nyq, ws=38/f_nyq, gpass=a_max, gstop=at, analog=False, ftype='butter', output='sos')
ecg_clean = sig.sosfiltfilt(bp_cheby,x)
"""
plt.figure("ECG LEAD MLII")
plt.plot(ecg_ii, label='ecg lead II')
#plt.plot(ECG_cheby_ii, label='IIR Butter II lead')
#plt.plot(x, label='filtro de mediana')
#plt.plot(ecg_clean,label='IIR Butter LPF')

plt.title('ECG LEAD II')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [mV]')
plt.grid(which='both', axis='both')

axes_ecg_ii = plt.gca()
axes_ecg_ii.legend()
"""
plt.figure("ECG LEAD V5")
plt.plot(ecg_v5, label='ecg lead V5')
#plt.plot(ECG_cheby_v5, label='IIR Butter V5 lead')

plt.title('ECG LEAD V5')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [mV]')
plt.grid(which='both', axis='both')

axes_ecg_v5 = plt.gca()
axes_ecg_v5.legend()
"""