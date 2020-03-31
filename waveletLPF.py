# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:38:21 2020

@author: crist
"""

import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt
import scipy.io as sio
import pywt

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


wavelet='db4'

coeff = pywt.wavedec(mlii,wavelet,level=8)
a=coeff
#coeff[1:] = (pywt.threshold(i, value=6,  ) for i in coeff[1:])
for i in range(1,len(coeff)):
    coeff[i]=pywt.threshold(coeff[i], value=6,  )


mlii_clean = pywt.waverec(coeff, wavelet , 'smooth')

"""
plt.figure("Coeficientes de detalle")
plt.plot(a[4],label='cd5')
plt.plot(a[3],label='cd6')
plt.plot(a[2],label='cd7')
plt.plot(a[1],label='cd8')
plt.title('Coeficiente de detalle')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [mV]')
plt.grid(which='both', axis='both')
axes_cd = plt.gca()
axes_cd.legend()
"""

#"""
plt.figure("ECG LEAD MLII")
#plt.plot(ecg_ii, label='lead II')
#plt.plot(qrs_det,ecg_ii[qrs_det],'x', label='detecciones de latidos')
plt.plot(mlii,label='lead II interpolada')
plt.plot(mlii_clean,label='lead II clean')


plt.title('ECG LEAD II')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [mV]')
plt.grid(which='both', axis='both')

axes_ecg_ii = plt.gca()
axes_ecg_ii.legend()
#"""
"""
x = np.linspace(0, 1, num=2048)
#chirp_signal = np.sin(250 * np.pi * x**2)
    
fig, ax = plt.subplots(figsize=(6,1))
ax.set_title("Original Chirp Signal: ")
ax.plot(mlii)#ax.plot(chirp_signal)
plt.show()
    
data = mlii#chirp_signal
waveletname = 'sym5'
 
fig, axarr = plt.subplots(nrows=10, ncols=2, figsize=(6,6))
for ii in range(10):
    (data, coeff_d) = pywt.dwt(data, waveletname)
    axarr[ii, 0].plot(data, 'r')
    axarr[ii, 1].plot(coeff_d, 'g')
    axarr[ii, 0].set_ylabel("Level {}".format(ii + 1), fontsize=14, rotation=90)
    axarr[ii, 0].set_yticklabels([])
    if ii == 0:
        axarr[ii, 0].set_title("Approximation coefficients", fontsize=14)
        axarr[ii, 1].set_title("Detail coefficients", fontsize=14)
    axarr[ii, 1].set_yticklabels([])
plt.tight_layout()
plt.show()
"""