# coding: utf-8
import numpy as np
# 数値を一つしか格納していないテンソルを「0階テンソル」、「スカラーテンソル」と呼ぶ
x = np.array(15)
print(x)
# データ型
print(x.dtype)
# 軸の数(階数)
print(x.ndim)