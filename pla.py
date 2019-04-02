import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import random

x_i_teste = [1,2,3,4]

w_i_teste = [100,200,300,400]

def a(lista_pesos,lista_x):
    
    total = 0

    dim = len(lista_pesos)
    
    if dim != len(lista_x):
        return "inconsistencia entre as dimensoes"

    for i in range(dim):
        total +=  lista_pesos[i]*lista_x[i]

    return total

x_b = [1,2,3,2,1]
y_b = [0,0,0,1,2]
x_r = [2,3,4,4,2]
y_r = [3,2,1,3,4]

# será que essa é a melhor forma de estruturar os dados?
pontos_classificados = [[1,0,-1,1],
                        [2,0,-1,1],
                        [3,0,-1,1],
                        [2,1,-1,1],
                        [1,2,-1,1],
                        [2,3,-1,0],
                        [3,2,-1,0],
                        [4,1,-1,0],
                        [4,3,-1,0],
                        [2,4,-1,0]]

#print (pontos_classificados)

#função para pegar um ponto aleatório da lista
def random_point(lista_pontos):
    return random.choice(lista_pontos)

#print (random_point(pontos_classificados))

reta_x_controle = np.linspace(0,5,100)
reta_y_controle = -1*(reta_x_controle)+4

epochs = 1000
learning_rate = 0.01

# função para testar se o ponto aleatório pegado foi corretamente classificado ou não tendo em vista a reta

def my_dot_product(a,b):
    
    total = 0

    for i in range(0,len(b)):
        
        total += a[i]*b[i]
    final_scalar = total
    return final_scalar

def ponto_acima_abaixo_reta(reta,ponto):
    
    total = 0

    coef_x_y = reta[0:2]
    coord_x_y = ponto[0:2]
    c_val = reta[-1]
    print("c_val",c_val)
    print ("my dot", my_dot_product(coef_x_y,coord_x_y))
    total = my_dot_product(coef_x_y,coord_x_y) - c_val
    print("total",total) 
    if total>=0:
        return 0
    else:
        return 1

#print (ponto_acima_abaixo_reta([1,1,4],[3,0,1]))
#print (ponto_acima_abaixo_reta([1,1,-4],[4,3,0]))
print (ponto_acima_abaixo_reta([1,1,4],[1,2,1]))

def classification_test(reta,ponto):

    sinal_oficial = ponto[-1]
    pos_rel_a_reta = ponto_acima_abaixo_reta(reta,ponto)

    if sinal_oficial==pos_rel_a_reta:
        return True
    else:
        return False
#print (classification_test([1,1,4],[4,3,0]))
#print (classification_test([1,1,4],[0,0,1]))
#print (classification_test([1,1,4],[0,0,0]))

def perceptron(reta,ponto):

    #se o ponto está corretamente classificado, não faz nada
    if classification_test(reta,ponto):
        return None
    #se o ponto está incorretamente classificado, muda os coeficientes do separador/reta
    else:
       if abaixo -> desloca para cima
            muda o coeficiente do c value
            plote as duas retas
       else (acima-> desloca para baixo)


#fazer uma reta inicial aleatória
coef_x_init = random.uniform(0,4)
coef_y_init = random.uniform(0,4)
c_val = random.uniform(0,4)
#print (coef_y_init,coef_x_init)
reta_x_iter = np.linspace(0,5,100)
reta_y_iter = (1/coef_y_init)*((coef_x_init*reta_x_iter)+c_val)

# plotar os pontos que tenho, a reta objetivo e a reta inicial aleatória
plt.plot(x_b, y_b, 'o', color='blue')
plt.plot(x_r, y_r, 'o', color='red')
plt.plot(reta_x_iter, reta_y_iter, '-g')
plt.plot(reta_x_controle,reta_y_controle,'-r')


plt.show()
