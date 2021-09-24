# coding: utf-8
import numpy as np
# 要素を縦、または横に一列に並べたものを「1階テンソル」、「ベクトル」と呼ぶ
x = np.array([1,2,3])
print(x)
# データ型
print(x.dtype)
# 軸の数(階数)
print(x.ndim)