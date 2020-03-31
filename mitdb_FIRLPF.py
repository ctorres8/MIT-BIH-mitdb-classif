# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:46:56 2020

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

#N_MLII = len(mlii)
#N_V5 = len(v5)
#N_QRS_II = len(qrs_ii)-2
#N_QRS_V5 = len(qrs_v5)-2


fs = 360 #Hz
f_nyq = fs/2 # 180 Hz

fc=40 #Hz
freqs= np.array([0 ,33, 36, 40 , f_nyq ])/f_nyq #Hz
gains = np.array([1 ,1, 10**(-3/20) , 0, 0])
#gains = 10**(gains/20)

N_Hamming=114 #round((8*f_nyq)/(fc1-fc0)) #114

#w_hamming = sig.firwin(N_Hamming, fc/f_nyq,window='hamming',)
w_hamming = sig.firwin2(N_Hamming, freq=freqs, gain=gains,window='hamming',)

#mlii_clean = sig.filtfilt(b,a,mlii)
#v5_clean = sig.filtfilt(b,a,v5)

mlii_clean = sig.filtfilt(w_hamming,[1],mlii)
v5_clean = sig.filtfilt(w_hamming,[1],v5)

#sio.savemat('ECG.mat',{'MLII':salida_ii,'V5':salida_v5,'QRS_DET_II':qrs_det_ii,'QRS_DET_V5':qrs_det_v5}) # Creo un archivo .mat para extraer las variables




plt.figure("ECG lead ")
plt.plot(mlii,label ='MLII')
plt.plot(mlii_clean, label = 'FIR Blackman')
#plt.plot(ECG_filtrada_w_Hamming, label = 'FIR Hamming')
plt.title('ECG')
plt.xlabel('Muestras')
plt.ylabel('Amplitud ')
plt.grid(which='both', axis='both')

axes_hdl_ECG = plt.gca()
axes_hdl_ECG.legend()



## RESP EN MODULO

w,H_Hamming = sig.freqz(w_hamming,[1]) #FIR HAMMING
w=(w/np.pi)*f_nyq #Normalizo a la frecuencia de Nyquist

###### PLOTEOS
plt.figure("Respuesta en frecuencia")

##PLOTEO FIR
plt.plot(w,20*np.log10(np.abs(H_Hamming)), label='fir Hamming')

plt.title('Respuesta en Frecuencia')
plt.xlabel('Frequencia normalizada a F de Nyquist')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')
#plt.axis([0, 75, -120, 5 ]);

Trazos = plt.gca()
Trazos.legend()
