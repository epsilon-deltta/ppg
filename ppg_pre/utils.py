import pandas as pd
def get_ppg_sample(idx=0):
    path = f'./sample/ppg{idx}.csv'
    df   = pd.read_csv(path,index_col=0)
    return df.to_numpy()