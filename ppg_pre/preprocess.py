import numpy as np
import pandas as pd

def interpolate(x :np.ndarray,mode='nearest')-> np.ndarray:

    if mode == 'nearest':
        x = pd.DataFrame(x,columns=['x'])
        x = x.fillna(method='ffill').fillna(method='bfill')
        x = x['x'].to_numpy()
    return x

def moving_average(x, w=30): # window
    return np.convolve(x, np.ones(w), 'valid') / w

from scipy import signal
def bandpass(x, band=[0.5,10], sample_rate=3000, order=101):
    fw = signal.firwin(order,band,fs=sample_rate,pass_zero='bandpass')
    x = signal.lfilter(fw,[1.0],x)
    return x

def moving_average(x, w): # window
    return np.convolve(x, np.ones(w), 'valid') / w

def norm_z(x,mean=47,std=15):
    return (x-mean)/std

from scipy import signal
def get_spectrogram(x,fs):
    f, t, xspec = signal.spectrogram(x, fs=fs)
    return xspec


def get_scalogram(x):
    pass

# ==== end2end ======
def ppg2specgram(x: np.numpy,sample_rate= 300):
    
    x = interpolate(x)
    x = bandpass(x, band=[0.5,10],sample_rate=sample_rate)
    x = moving_average(x,w=30)
    x = norm_z(x)
    f, t, xspec = get_spectrogram(x,fs=sample_rate)
    return xspec
    
    