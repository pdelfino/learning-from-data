import random

moeda = ["cara","coroa"]

#print (random.choice(coin))
#função que joga uma moeda dez vezes

def flip_10_times(coin):
    
    resultados = []

    for i in range(1,11):
        
        resultados.append(random.choice(coin))

    return resultados

print (flip_10_times(moeda))

t_fix_lanc_10_vzs_mesma_moeda = ['cara', 'cara', 'cara', 'cara', 'coroa',
                                 'coroa', 'cara', 'coroa', 'coroa', 'cara']

print(t_fix_lanc_10_vzs_mesma_moeda)













'''

def count_caras(resul_dez_lançamentos):

    count = 0

    for i in resul_dez_lançamentos:
    
        if i=="cara":
        
            count+=1

    total_count = count
    
    return total_count

#print (count_caras(t_fix_lanc_10_vzs_mesma_moeda))


#função que joga 1000 moedas na função acima

def simulation_1000_coins(coin):

    matriz_resultados = []

    for i in range(1,1001):
        
        dez_vezes_a_moeda = flip_10_times(coin)
        matriz_resultados.append([i,dez_vezes_a_moeda])

    return matriz_resultados

print (simulation_1000_coins(moeda))


def c_first(matriz):

    return matriz[0]

#print (c_first(simulation_1000_coins(moeda)))

def c_rand(matriz):

    return random.choice(matriz)

#print (c_rand(simulation_1000_coins(moeda)))
    

def freq_car(resultado_10_lançamentos):
    
    count_coroas = 0

    for i in resultado_10_lançamentos:
        
        if i=="cara":
        
            count_caras=0
'''
