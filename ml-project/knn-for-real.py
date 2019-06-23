import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

# no arquivo de dados são 11 variáveis, 10 independetes e 1 dependente?
df = pd.read_csv('breast-cancer-wisconsin.data.txt')

df.replace('?',-99999, inplace=True)

df.drop(['id'], 1, inplace=True)

# as features são tudo menos a coluna de classe
X = np.array(df.drop(['class'], 1))

y = np.array(df['class'])

# fazer a cross validation, usando os dados de treinamento pra estimar os parâmetros
# separar nos conjuntos de treino e de teste, para depois descobrir a acurácia
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.3)

clf = neighbors.KNeighborsClassifier(26)

# inserir no objeto o treinamento
clf.fit(X_train, y_train)

# fazer o teste para saber a acurácia
accuracy = clf.score(X_test, y_test)
print("acurácia: ",accuracy)

#exemplo pra prever se a célula é benigna ou maligna
example_measures = np.array([4,2,1,1,1,2,3,2,1])
example_measures = example_measures.reshape(1, -1)
prediction = clf.predict(example_measures)
print("predição: ",prediction)
