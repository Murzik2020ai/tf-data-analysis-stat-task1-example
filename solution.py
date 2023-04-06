import pandas as pd
import numpy as np


chat_id = 1226526788

def solution(x: np.array) -> float:
    df = pd.DataFrame({'value':x})
    df['value'] = df['value'] - 779
    df['value'] = df['value'].apply(np.log)
    return df.value.mean()
