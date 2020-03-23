#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

data = pd.read_csv('tic-tac-toe.data', sep=',')

arr1 = data['1']
arr2 = data['2']
arr3 = data['3']
arr4 = data['4']
arr5 = data['5']
arr6 = data['6']
arr7 = data['7']
arr8 = data['8']
arr9 = data['9']
arr_res = data['result']

X_wins = np.where(data['result'] == 'positive')

x1 = len(arr1[(arr1 == 'x') & (arr_res == 'positive')])
o1 = len(arr1[(arr1 == 'o') & (arr_res == 'positive')])
b1 = len(arr1[(arr1 == 'b') & (arr_res == 'positive')])

x2 = len(arr2[(arr2 == 'x') & (arr_res == 'positive')])
o2 = len(arr2[(arr2 == 'o') & (arr_res == 'positive')])
b2 = len(arr2[(arr2 == 'b') & (arr_res == 'positive')])

x3 = len(arr3[(arr3 == 'x') & (arr_res == 'positive')])
o3 = len(arr3[(arr3 == 'o') & (arr_res == 'positive')])
b3 = len(arr3[(arr3 == 'b') & (arr_res == 'positive')])

x4 = len(arr4[(arr4 == 'x') & (arr_res == 'positive')])
o4 = len(arr4[(arr4 == 'o') & (arr_res == 'positive')])
b4 = len(arr4[(arr4 == 'b') & (arr_res == 'positive')])

x5 = len(arr5[(arr5 == 'x') & (arr_res == 'positive')])
o5 = len(arr5[(arr5 == 'o') & (arr_res == 'positive')])
b5 = len(arr5[(arr5 == 'b') & (arr_res == 'positive')])

x6 = len(arr6[(arr6 == 'x') & (arr_res == 'positive')])
o6 = len(arr6[(arr6 == 'o') & (arr_res == 'positive')])
b6 = len(arr6[(arr6 == 'b') & (arr_res == 'positive')])

x7 = len(arr7[(arr7 == 'x') & (arr_res == 'positive')])
o7 = len(arr7[(arr7 == 'o') & (arr_res == 'positive')])
b7 = len(arr7[(arr7 == 'b') & (arr_res == 'positive')])

x8 = len(arr8[(arr8 == 'x') & (arr_res == 'positive')])
o8 = len(arr8[(arr8 == 'o') & (arr_res == 'positive')])
b8 = len(arr8[(arr8 == 'b') & (arr_res == 'positive')])

x9 = len(arr9[(arr9 == 'x') & (arr_res == 'positive')])
o9 = len(arr9[(arr9 == 'o') & (arr_res == 'positive')])
b9 = len(arr9[(arr9 == 'b') & (arr_res == 'positive')])


plt.clf()

f, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3,3)

labels = 'x', 'o', 'b'

ax1.pie([x1, o1, b1], labels=labels)
ax2.pie([x2, o2, b2], labels=labels)
ax3.pie([x3, o3, b3], labels=labels)
ax4.pie([x4, o4, b4], labels=labels)
ax5.pie([x5, o5, b5], labels=labels)
ax6.pie([x6, o6, b6], labels=labels)
ax7.pie([x7, o7, b7], labels=labels)
ax8.pie([x8, o8, b8], labels=labels)
ax9.pie([x9, o9, b9], labels=labels)

plt.show()

    
    
    
        
    
    
    
    

