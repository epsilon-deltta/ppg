# ppg
ppg preprocessing (e.g., ppg> spectogram, bandpass, moving average)

ALL in One: Simple PPG preprocessing 

# Usage

Installation
```
pip install ppg-pre
```

python usage
```
from ppg_pre import get_ppg_sample
x = get_ppg_sample() # get sample ppg data

from ppg_pre import ppg2specgram
x = ppg2specgram(x) # u can get the spectrogram data
```

# Function

ppg2specgram function has the following processing.

- interpolate
- bandpass (0.5~10 Hz)
- moving average (30 taps)
- z-score normalization (mean:47, std:15)
- spectrogram
