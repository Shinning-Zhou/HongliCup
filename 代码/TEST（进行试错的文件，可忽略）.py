import matplotlib.pyplot as plt
import pywt
import pandas as pd
import numpy as np

plt.rcParams['font.family']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.sans-serif'] = ['SimHei']#正常显示标签

path1 = r"D:\HongliCup\题目B\高成本传感器数据\High quality sensor 02.csv"
df = pd.read_csv(path1)
index = df['Time (s)']
data = df['Acceleration x (m/s^2)']

# Create wavelet object and define parameters
w = pywt.Wavelet('db4')  # 选用Daubechies8小波
maxlev = pywt.dwt_max_level(len(data), w.dec_len)
print("maximum level is " + str(maxlev))
threshold = 0.08  # Threshold for filtering

# Decompose into wavelet components, to the level selected:
coeffs = pywt.wavedec(data, 'db4', level=4)  # 将信号进行小波分解
print(coeffs.tolist())