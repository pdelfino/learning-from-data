import random
import operator

moeda = ["cara","coroa"]

#print (random.choice(coin))
#função que joga uma moeda dez vezes

def flip_10_times(coin):
    
    resultados = []

    for i in range(1,11):
        
        resultados.append(random.choice(coin))

    return resultados

#print (flip_10_times(moeda))

t_fix_lanc_10_vzs_mesma_moeda = ['cara', 'cara', 'cara', 'cara', 'coroa',
                                 'coroa', 'cara', 'coroa', 'coroa', 'cara']

#print(t_fix_lanc_10_vzs_mesma_moeda)

def count_caras(listao_com_10_lancamentos):
    
    count = 0

    for i in listao_com_10_lancamentos:
        for j in i:
            if j=="cara":
                count+=1
    return count

listao_10_lancamentos = [
        ['coroa', 'coroa', 'coroa', 'coroa', 'cara', 'coroa', 'coroa', 'cara', 'cara', 'coroa'],
        ['cara', 'cara', 'cara', 'coroa', 'cara', 'cara', 'cara', 'cara', 'cara', 'cara'],
        ['cara', 'coroa', 'cara', 'cara', 'cara', 'cara', 'cara', 'cara', 'coroa', 'coroa'],
        ['coroa', 'coroa', 'cara', 'cara', 'cara', 'cara', 'cara', 'coroa', 'cara', 'coroa'],
        ['coroa', 'cara', 'coroa', 'cara', 'cara', 'coroa', 'cara', 'coroa', 'coroa', 'coroa'],
        ['coroa', 'cara', 'cara', 'cara', 'coroa', 'coroa', 'coroa', 'coroa', 'cara', 'coroa'],
        ['coroa', 'coroa', 'coroa', 'cara', 'cara', 'cara', 'cara', 'cara', 'coroa', 'coroa'],
        ['coroa', 'cara', 'coroa', 'coroa', 'cara', 'coroa', 'coroa', 'coroa', 'coroa', 'coroa'],
        ['coroa', 'coroa', 'coroa', 'coroa', 'coroa', 'coroa', 'cara', 'coroa', 'coroa', 'cara'],
        ['cara', 'cara', 'cara', 'coroa', 'coroa', 'coroa', 'coroa', 'cara', 'coroa', 'cara']]

#print (count_caras(listao_10_lancamentos))

def sacola_dez_moedas(coin):

    dict_resultados = {}
    
    for i in range(1,1001):
        count_caras_iter = 0
        lista_iter_10_lancamentos = []
        
        for j in range(1,11):
            
            lista_iter_10_lancamentos.append(flip_10_times(coin))

        count_caras_iter = count_caras(lista_iter_10_lancamentos)
        dict_resultados[str(i)]= (lista_iter_10_lancamentos, count_caras_iter)
#    print (dict_resultados)
    return dict_resultados

sacolao_fix = {'1': ([['cara', 'cara', 'cara', 'cara', 'cara', 'coroa', 'coroa', 'cara', 'cara', 'cara'], 
               ['coroa', 'coroa', 'cara', 'cara', 'coroa', 'cara', 'coroa', 'cara', 'coroa', 'coroa'], 
               ['cara', 'cara', 'cara', 'coroa', 'coroa', 'coroa', 'coroa', 'coroa', 'cara', 'coroa'],
               ['coroa', 'cara', 'cara', 'cara', 'cara', 'coroa', 'coroa', 'cara', 'cara', 'coroa'], 
               ['coroa', 'coroa', 'cara', 'coroa', 'coroa', 'cara', 'cara', 'coroa', 'coroa', 'cara'],
               ['cara', 'coroa', 'cara', 'cara', 'cara', 'cara', 'cara', 'cara', 'cara', 'coroa'], 
               ['cara', 'coroa', 'coroa', 'cara', 'coroa', 'coroa', 'coroa', 'cara', 'cara', 'cara'],
               ['coroa', 'coroa', 'cara', 'coroa', 'cara', 'cara', 'coroa', 'coroa', 'cara', 'cara'],
               ['coroa', 'cara', 'coroa', 'coroa', 'cara', 'cara', 'cara', 'coroa', 'coroa', 'cara'],
               ['coroa', 'cara', 'coroa', 'coroa', 'cara', 'coroa', 'cara', 'coroa', 'cara', 'coroa']],
               53), 
               '2': ([['coroa', 'cara', 'cara', 'coroa', 'cara', 'cara', 'coroa', 'coroa', 'cara', 'cara'],
                ['cara', 'cara', 'coroa', 'cara', 'cara', 'coroa', 'coroa', 'cara', 'coroa', 'coroa'],
                ['coroa', 'coroa', 'coroa', 'cara', 'coroa', 'cara', 'cara', 'coroa', 'cara', 'cara'],
                ['coroa', 'coroa', 'coroa', 'coroa', 'cara', 'cara', 'coroa', 'cara', 'coroa', 'coroa'],
                ['cara', 'cara', 'coroa', 'coroa', 'cara', 'cara', 'coroa', 'coroa', 'coroa', 'coroa'],
                ['cara', 'coroa', 'cara', 'coroa', 'cara', 'coroa', 'cara', 'cara', 'coroa', 'cara'],
                ['coroa', 'cara', 'cara', 'coroa', 'coroa', 'cara', 'coroa', 'cara', 'cara', 'cara'],
                ['cara', 'cara', 'coroa', 'coroa', 'coroa', 'coroa', 'coroa', 'cara', 'cara', 'coroa'],
                ['coroa', 'coroa', 'cara', 'coroa', 'coroa', 'cara', 'cara', 'cara', 'cara', 'coroa'],
                ['coroa', 'cara', 'coroa', 'coroa', 'cara', 'cara', 'coroa', 'coroa', 'coroa', 'cara']],
                48), 
               '3': ([['coroa', 'cara', 'cara', 'cara', 'cara', 'cara', 'coroa', 'coroa', 'cara', 'coroa'],
                ['cara', 'coroa', 'coroa', 'cara', 'cara', 'coroa', 'coroa', 'coroa', 'cara', 'cara'], 
                ['coroa', 'coroa', 'coroa', 'cara', 'coroa', 'cara', 'coroa', 'cara', 'cara', 'cara'],
                ['coroa', 'coroa', 'cara', 'coroa', 'cara', 'coroa', 'cara', 'coroa', 'coroa', 'cara'],
                ['cara', 'coroa', 'coroa', 'coroa', 'coroa', 'cara', 'cara', 'coroa', 'cara', 'coroa'], 
                ['coroa', 'coroa', 'cara', 'coroa', 'coroa', 'cara', 'coroa', 'cara', 'coroa', 'cara'],
                ['cara', 'coroa', 'coroa', 'coroa', 'cara', 'coroa', 'cara', 'cara', 'coroa', 'cara'],
                ['cara', 'coroa', 'cara', 'coroa', 'cara', 'coroa', 'cara', 'cara', 'coroa', 'coroa'],
                ['cara', 'cara', 'coroa', 'coroa', 'coroa', 'cara', 'coroa', 'coroa', 'coroa', 'cara'], 
                ['cara', 'coroa', 'coroa', 'cara', 'coroa', 'cara', 'coroa', 'coroa', 'cara', 'coroa']],
                46)}

def c_min(sacolao):
    
    lista_valores_minimos = []
    
    for i,j in sacolao.items():
        lista_valores_minimos.append(j[1])

    return min(lista_valores_minimos)

print (c_min(sacola_dez_moedas(moeda)))

simulation = []

for i in range(1,1001):
    simulation.append(c_min(sacola_dez_moedas(moeda)))

print (sum(simulation)/len(simulation))
