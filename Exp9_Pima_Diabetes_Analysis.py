import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import statistics

df = pd.read_csv('Pima2.csv')
print(df.describe().T)
df.plot(kind='density', subplots=True, layout=(3,3), sharex=False)

preg = np.array(df['npreg'])
print('Pregnancies Mean:', statistics.mean(preg))
print('Skewness:', skew(preg))
print('Kurtosis:', kurtosis(preg))

G = np.array(df['glu'])
print('Glucose Mean:', statistics.mean(G))
print('Skewness:', skew(G))
print('Kurtosis:', kurtosis(G))
