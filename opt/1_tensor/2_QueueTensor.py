# coding: utf-8
import numpy as np
# 1階テンソルを縦、横に組み合わせたものを「2階テンソル」、「行列」と呼ぶ
x = np.array([[1,2,3,4,5],
             [10,20,30,40,50],
             [100,200,300,400,500]])
print(x)
# データ型
print(x.dtype)
# 軸の数(階数)
print(x.ndim)