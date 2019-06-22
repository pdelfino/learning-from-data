import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
#print(df.head())  

#df["bare_nuclei"].hist()
df["class"].hist()


#x = df["class"].hist()
#plt.xticks(x, ['a','c'])

plt.title('Maligno versus Benigno')
plt.ylabel('Frequência')
plt.figtext(.75, .01, "4 = Tumor Maligno")
plt.figtext(.15, .01, "2 = Benigno")
plt.show()

'''
for i in df:
    print (i)
    print (df[str(i)].describe())
    print (" ")

excluí o primeiro e último resultado do print pq era o ID e o output final
sobre ser maligno ou benigno
'''
