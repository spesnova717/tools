# -*- coding: utf-8 -*-
import os
import ntpath
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# 読み込むCSVファイルのパス
csv_path = "./test.csv"

# グラフ画像の保存先パス
save_path = "./"

# 空のデータフレームを作成
df = pd.DataFrame({})

# CSVファイルのロードし、データフレームへ格納
df = pd.read_csv(csv_path, encoding="UTF-8", skiprows=0)

# %CPUの列データを取り出し
cpu = df.loc[:, "%CPU"]

# 経過時間の列データを取り出し
times = df.loc[:, "TIME"]

cpu_rm = cpu.rolling(5).mean()

# 保存先パスが存在しなければ作成
if not os.path.exists(save_path):
       os.mkdir(save_path)

# グラフ化
ax = plt.axes()
plt.rcParams['font.family'] = 'Times New Roman'  # 全体のフォント
plt.rcParams['axes.linewidth'] = 1.0  # 軸の太さ

# %CPUをプロット
plt.plot(times, cpu, lw=1, c="r", alpha=0.7, ms=2, label="%CPU(t)")

# %CPU移動平均をプロット
plt.plot(times, cpu_rm, lw=1, c="b", alpha=0.7, ms=2, label="%CPU_Rm(t)")

# グラフの保存
plt.legend(loc="best")     # 凡例の表示（2：位置は第二象限）
plt.xlabel('Time[sec]', fontsize=12)  # x軸ラベル
plt.ylabel('CPU[%]', fontsize=12)  # y軸ラベル
plt.grid()  # グリッドの表示
plt.legend(loc="best")  # 凡例の表示
plt.savefig(save_path + "current.png")
plt.clf()
