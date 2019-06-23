# Trabalho de ML

#### *Construindo um modelo preditivo de classificação de tumores de mama*



O relatório do trabalho será feito neste arquivo Markdown e por meio de respostas às perguntas do [arquivo](https://www.dropbox.com/s/pnc02xjuotf7q0y/Trabalho.pdf?dl=0) com instruções.



#### Disclaimer

Antes de iniciar a resolução, cabe indicar os materiais de consulta. Durante a execução do trabalho, senti que estava um pouco despreparado para tarefas intermediárias como obtenção dos dados, limpeza, treinamento do modelo e teste. Assim, busquei materiais de consulta **com abordagens práticas**, entre eles, destaco:

- repositório do professor Renato Souza da EMAp, em especial, o *case* da ISIS [link]
- vídeo ISIS [link]
- playlist do sentdex [link]
- stackoverflow: perguntas diversas feitas por outros usuários e uma pergunta que eu mesmo fiz [link]



## Parte 1: Introdução



#### 1.1 - Descreva a base em conjunto com sua *pergunta de pesquisa*



A base de dados vem de um repositório da **UC Irvine Machine Learning Repository** [link](https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/).

Os dados descrevem atributos de células cancerígenas na região da mama, sendo o ponto principal a indicação de uma classificação entre tumores malignos e benignos.

A pergunta de pesquisa que se pretende responder é: *em qual nível de acurácia um modelo preditivo consegue classificar um tumor, na região da mama, como benigno ou maligo?*

#### 1.2 - Apresente a base de dados e a dependência de suas variáveis



Os principais aspectos da base são:



-  A amostra é formada por 699 elementos

- Ao todo são 11 colunas/atributos na base de dados, sendo que uma delas é apenas um identificador (ID) e a última delas apresenta a classificação como Benigno ou Maligno. Para tumores benignos, o número 2 é usado. Para tumores malignos, o número 4 é usado.

  De acordo com a documentação, essas são as variáveis:

  ```tex
  
     #  Attribute                     Domain
     -- -----------------------------------------
     1. Sample code number            id number
     2. Clump Thickness               1 - 10
     3. Uniformity of Cell Size       1 - 10
     4. Uniformity of Cell Shape      1 - 10
     5. Marginal Adhesion             1 - 10
     6. Single Epithelial Cell Size   1 - 10
     7. Bare Nuclei                   1 - 10
     8. Bland Chromatin               1 - 10
     9. Normal Nucleoli               1 - 10
    10. Mitoses                       1 - 10
    11. Class:                        (2 for benign, 4 for malignant)
  
  ```

- A única variável dependente é `Class`. As outras  colunas como `Normal Nucleoli` e etc são modeladas como variáveis independentes, com uma única exceção: a coluna `Sample code number` não é uma variável no modelo. Ela serve apenas como apoio para a manipulação dos dados.

  

  Por fim, há de ser ressaltado que o problema a ser tratado neste trabalho é a construção de um modelo preditivo de classificação de tumores como malignos ou benignos **usando o método de KNN**.



#### 1.3 Apresente estatísticas descritivas da base



Por meio de um script simples em Python foram geradas estatísticas descritivas relevantes para compreensão do contexto:

```python
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data.txt')

for i in df:
    print (i)
    print (df[str(i)].describe())
    print (" ")

```



As estatísticas descritivas relevantes da base de dados são:

```
clump_thickness
count    699.000000
mean       4.417740
std        2.815741
min        1.000000
25%        2.000000
50%        4.000000
75%        6.000000
max       10.000000
Name: clump_thickness, dtype: float64

unif_cel_size
count    699.000000
mean       3.134478
std        3.051459
min        1.000000
25%        1.000000
50%        1.000000
75%        5.000000
max       10.000000
Name: unif_cel_size, dtype: float64

unif_cel_shape
count    699.000000
mean       3.207439
std        2.971913
min        1.000000
25%        1.000000
50%        1.000000
75%        5.000000
max       10.000000
Name: unif_cel_shape, dtype: float64

marg_adhesion
count    699.000000
mean       2.806867
std        2.855379
min        1.000000
25%        1.000000
50%        1.000000
75%        4.000000
max       10.000000
Name: marg_adhesion, dtype: float64

single_epith_cell_size
count    699.000000
mean       3.216023
std        2.214300
min        1.000000
25%        2.000000
50%        2.000000
75%        4.000000
max       10.000000
Name: single_epith_cell_size, dtype: float64

bare_nuclei
count     699
unique     11
top         1
freq      402
Name: bare_nuclei, dtype: object

bland_chrom
count    699.000000
mean       3.437768
std        2.438364
min        1.000000
25%        2.000000
50%        3.000000
75%        5.000000
max       10.000000
Name: bland_chrom, dtype: float64

norm_nucleoli
count    699.000000
mean       2.866953
std        3.053634
min        1.000000
25%        1.000000
50%        1.000000
75%        4.000000
max       10.000000
Name: norm_nucleoli, dtype: float64

mitoses
count    699.000000
mean       1.589413
std        1.715078
min        1.000000
25%        1.000000
50%        1.000000
75%        1.000000
max       10.000000
Name: mitoses, dtype: float64

```



#### 1.4 Apresente outra duas análises ou visualizações interessantes



- Como descrito na documentação a distribuição, na amostra, de tumores benignos e malignos é:

  ​	Benign: 458 (65.5%)
  ​	Malignant: 241 (34.5%)

Assim, decidi plotar os dados por meio do script:



```python
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
```



O código retorna a seguinte image:

![](/home/pedro/lfd/ml-project/visu-central-info.png)







A imagem acima não é muito interessante, mas expressa bem a proporção da questão crucial que está em jogo.



Mais interessante do que isso, são as duas vizualizações abaixo. A história por trás da visualização será apresentada a seguir é peculiar.



Meu pai é médico, com residência em cirurgia geral. Estou em BH e, um dia, comentei do trabalho que estava fazendo, que envolvia tumores de mama.  Ele me disse que achava que o tamanho do tumor seria já um bom indicativo para descobrir se é maligno ou benigno. 



Dito isso, fiz um histograma em relação ao tamanho dos tumores e uma separação por cores. Para isso, usei a variável  `Uniformity of Cell Size`.  Essa variável vai de 1 a 10, sendo 10 uma célular bem grande. De fato, a hipótese/intuição do meu pai, que tem alguma familiaridade com o domínio, estava certa rsrs. Como o histograma indica abaixo,  tumores malignos tendem a ser maiores que benignos:

![](/home/pedro/lfd/ml-project/histogram-cell-size.png)

![size-maligno-benigno](/home/pedro/lfd/ml-project/size-maligno-benigno.png)



O código usado para essas visualizações é:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
print(df.head())  
#df['unif_cel_size'].hist()
df.groupby('class')['unif_cel_size'].plot(kind='hist',legend=True)
plt.show()

```



#### 1.5 Proporção de treino e de teste

Dividi os meus dados aleatoriamente na proporção de 70-30, sendo que 70% para treinamento e 30% para teste.



# Parte 2: Metodologia 



#### 2.1 Indicação das variáveis dependentes e independentes que serão usadas

Como dito acima, as variáveis dependentes são:

- `Clump Thickness   `
- `Uniformity of Cell Size  `

- `Uniformity of Cell Shape `
- `Marginal Adhesion  `
- `Single Epithelial Cell Size `
- `Bare Nuclei `
- `Bland Chromatin `
- `Normal Nucleoli  `
- `Mitoses` 

A única variável independente será:

- `Class`        

Como dito anteriormente, a variável `Sample code number` serve apenas como ferramenta de manipulação dos dados.



#### 2.2 Identificação do hiperparâmetro



O método usado será o KNN. Desse modo, existe um único hiperparâmetro a ser definido: o k-número de vizinhos que serão  considerados.



Seguindo as recomendações de boas práticas que percebi no conteúdo prático citado acima, a recomendação é de usar a raiz quadrada do tamanho da amostra, isto é: 

$ \sqrt[n]{k} $

No caso, como a amostra é n = 699. Temos a raiz aproximada de k = 26.



#### 2.3 Utilize k-fold cross validation

#### 2.4 Construa o gráfico com erro de validação cruzada

#### 2.5 Plote a fronteira de decisão para o hiperparâmetro escolhido

Não é possível tendo em  vista que são 10 variáveis em jogo. Conversei com a colega Vitória sobre isso.

De acordo com ela, existem técnicas para plotar a fronteira de decisão em casos que vão além do plano de duas dimensões, mas não foi explorar essas técnicas para esse trabalho.



#### 2.6 Apresente os erros dentro da amostra, de validação cruzada e de teste



# Parte 3: Conclusão













