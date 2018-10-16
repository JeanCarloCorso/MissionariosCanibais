import random
from time import time
import numpy
ma = ['p', 'p', 'p', 'c', 'c', 'c']
mo = ['o','o','o','o','o','o']
opcoesBote = [
        [0,1], #coluna 0 padres coluna 1 canibais
        [1,0],
        [1,1],
        [0,2],
        [2,0]
    ]

def reconstituicao(j, solucao):
    ma = ['p', 'p', 'p', 'c', 'c', 'c']
    mo = ['o','o','o','o','o','o'] 

    print("\n\n------------Matrizes zeradas------------\n\n")

    for i in range(0, j):
        if(i % 2 == 0):
            jogada(1,opcoesBote[solucao[j]][0],opcoesBote[solucao[j]][1])
        else:
            jogada(0,opcoesBote[solucao[j]][0],opcoesBote[solucao[j]][1])

def mostraJoagada(ma,mo):
    print("ma",ma)
    print("mo",mo)
    contaObjetivoAtingido(mo)
    contaMorte(ma,mo)

def NumeroPC(m):#numero de padres e canibais na matriz

    np = 0 #numero de padres
    nc = 0 #numero de canibais

    for i in m:
        if i == 'p':
            np = np + 1
        if i == 'c':
            nc = nc + 1

    return np, nc

def TamanhoPC(m):
    npo,nco=padresCanibais(m) #na matriz
    tamMo=npo+nco
    return tamMo

def testeObjetivoAtingido(mo):
    #objetivo atingido retorna 1
    #objetivo não atingido retona 0
    np,nc=NumeroPC(mo)
    if(np==3 and nc==3):
        return 1
    else:
        return 0

def contaObjetivoAtingido(mo):
    if(testeObjetivoAtingido(mo)==1):
        print("OBJETIVO ATINGIDO")
        return 1
    print("Objetivo nao atingido")
    return 0

def testeMorte(ma,mo):
    #se retornar "0" padres são devorados
    #se retornar "1" padres estão salvos
    retorno = 1
    pma, cma = NumeroPC(ma)#numero de padres e canibais em lado atual
    if(pma<cma and pma!=0):
        retorno = 0
    pmo,cmo=NumeroPC(mo)#numero de padres e canibais em lado oposto
    if(pmo<cmo and pmo!=0):
        retorno = 0
    
    return retorno #retornando zero a aternativa deve ser desprezada retornando 1 é válida

def contaMorte(ma,mo):
    vivo=testeMorte(ma,mo)
    if(vivo==1):
        print("Os padres estão vivos")
    else:
        print("Há padres mortos\n----------------------------------------------")

def boteAO(np, nc):#bote de atual para oposto np número de padres nc número de canibais
    npo = npa = np
    nco = nca = nc
    
    for i in range(0, 6):# por padre em mo
        if npo != 0 and mo[i]!='p' and mo[i]!='c':
            mo[i] = 'p'
            npo=npo-1

    for i in range(0, 6):# por canibais em mo
        if nco != 0 and mo[i]!='p' and mo[i]!='c':
            mo[i] = 'c'
            nco=nco-1
                
    for i in range(0,6):
        if(ma[i]=='p' and npa>0):
            ma[i]='o'
            npa = npa -1

    for i in range(0,6):
        if(ma[i]=='c' and nca>0):
           ma[i]='o'
           nca = nca -1     
    return 0

def boteOA(np, nc): #bote de oposto para atual
    npo = npa = np
    nco = nca = nc
    for i in range(0,6):
        if npo != 0 and ma[i] != 'p' and ma[i] != 'c':
            ma[i] = 'p'
            npo = npo - 1
    for i in range(0,6):
        if nco!=0 and ma[i]!='p' and ma[i]!='c':
            ma[i]='c'
            nco=nco-1
    for i in range(0,6):
        if (mo[i]=='p' and npa!=0):
            mo[i]='o'
            npa = npa-1
    for i in range(0,6):
        if(mo[i]=='c' and nca!=0):
            mo[i]='o'
            nca=nca-1
    return 0

def jogada(sentido,x,y):
    if(sentido==1):
        boteOA(x,y)
    else:
        boteAO(x,y) 

def escolheTripulacao():
    solucao = []
    for i in range(0,15):
        solucao.append('nul')
    ops = 0
    prox = False
    refaz = False
    j = -1 #jogada
    for i in range(0,5000):
        j += 1
        if j > 6:
            j -= 1
            prox = True
        
        if(prox == True):
            ops += 1
            prox = False
            if(ops > 4):
                j -= 1
                for i in range(j, -1, -1):
                    if(solucao[i] < 4):
                        solucao[i] += 1
                        j = i + 1
                        ops = 0
                        break

        solucao[j] = ops
        

        if(j % 2 > 0):
            np, nc = NumeroPC(mo)
            if((np >= opcoesBote[solucao[j]][0])or(nc >= opcoesBote[solucao[j]][1])):
                print("\noa \n[",opcoesBote[solucao[j]][0],",",opcoesBote[solucao[j]][1],"]\n")
                jogada(1,opcoesBote[solucao[j]][0],opcoesBote[solucao[j]][1])
            else:
                refaz = True
        elif(j % 2 == 0):
            np, nc = NumeroPC(ma)
            if((np >= opcoesBote[solucao[j]][0])or(nc >= opcoesBote[solucao[j]][1])):
                print("\nao \n[",opcoesBote[solucao[j]][0],",",opcoesBote[solucao[j]][1],"]\n")
                jogada(0,opcoesBote[solucao[j]][0],opcoesBote[solucao[j]][1])
            else:
                refaz = True

        mostraJoagada(ma,mo)
        
        if(contaObjetivoAtingido(mo) == 1):
            print(solucao)
            print("\npppppp\n")
            break

        if(testeMorte(ma,mo)==0 or refaz == True):
            prox = True
            #print(solucao)
            solucao[j] = 'nul'
            j -= 1
            reconstituicao(j,solucao)

        if(j <= 0):
            j = 0
        print(solucao)
    return solucao

def main():
    print("boteAO(p,c)")
    mostraJoagada(ma,mo)
    solucao = escolheTripulacao()
    print(solucao)


main()
