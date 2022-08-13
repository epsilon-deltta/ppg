import pandas as pd
import os

cur_dir = os.path.dirname(os.path.realpath(__file__))

def get_ppg_sample(idx=0):

    path = os.path.join(cur_dir, f'./sample/ppg{idx}.csv')
    df   = pd.read_csv(path,index_col=0)
    return df.to_numpy()