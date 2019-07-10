import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

style.use('fivethirtyeight')

data_set = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}

'''
############################################################### essa parte aqui printa: k e r
#[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in data_set[i]] for i in data_set]
######################################### essa parte printa as listas do k, depois as listas do r
for i in data_set:
    print (i)

for ii in data_set['k']:
    print (ii)

for ii in data_set['r']:
    print (ii)

for i in data_set:
    for ii in data_set[i]:
        plt.scatter(ii[0],ii[1],s=100,color=i) 
plt.show()

#############
'''

df = pd.read_csv('breast-cancer-wisconsin.data.txt')

df.replace('?',-99999, inplace=True)

unif_cel_size = df['unif_cel_size']
#print (unif_cel_size)

marg_adhesion = df['marg_adhesion']
#print (marg_adhesion)

classif = df['class']
#print (classif)

vals = []

for i in range(0,len(classif)):
    vals.append([unif_cel_size[i],marg_adhesion[i],classif[i]])

# criar dicionário
# iterar sobre vals, se terminar em 2, adicionar à parte com 2, se terminar em 4, adicionar à parte maligno

for i in vals:
    if i[2]==2:

        plt.scatter(i[0],i[1],color='b')
    elif i[2]==4:
        plt.scatter(i[0],i[1],color='r')
plt.xlabel('uniform cell')
plt.ylabel('marginal adhesion')
plt.title('Fronteira de decisão para 2 variáveis')
plt.show()
