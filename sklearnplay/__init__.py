# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 22:22
# @Author  : dzzxjl@126.com
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


y_true = [1, 2]
y_pred = [1, 3]
print(mean_squared_error(y_true, y_pred))
