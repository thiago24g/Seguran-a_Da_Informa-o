"""
@Autores Felipe e Thiago

Versão 1.4

Cifra de PlayFair
"""

import os

#Remover elementos Repetidos da lista
def removerRepeticoes(l):
    dict = {}
    for word in l:
        dict[word] = 1
    l[:] = dict.keys()
    return l

#Realiza o mapeamento da matriz, para evitar busca de posições em loops
def mapear(matriz):
    dict = {}
    for i in range(0,5):
        for j in range(0,5):
            dict[matriz[i][j]] = [i,j]
    return dict
    
#Monta a matriz 5x5
def montarMatriz(l):
    aux=0
    matriz=[]
    for i in range(0,5):
        temp=[]
        for j in range(0,5):
            temp.append(l[aux])
            aux+=1
        matriz.append(temp)
    return matriz

#Retorna a posicao do elemento informado - Obsoleto
"""def posicao(e, matriz):
    pos=[]
    for i in range(0,5):
        for j in range(0,5):
            if matriz[i][j] == e:
                pos.append(i)
                pos.append(j)
                break
    return pos """

#Realiza a criptografia do texto
def criptografar(let1, let2, m, dict):
    pos1=dict[let1]
    pos2=dict[let2]
    temp=''
    if pos1[0] == pos2[0]:
        temp+=m[pos1[0]][(pos1[1]+1)%5]
        temp+=m[pos2[0]][(pos2[1]+1)%5]
    elif pos1[1] == pos2[1]:
        temp+=m[(pos1[0]+1)%5][pos1[1]]
        temp+=m[(pos2[0]+1)%5][pos2[1]]
    else:
        temp+=m[pos1[0]][pos2[1]]
        temp+=m[pos2[0]][pos1[1]]
    return temp

#Descriptografa o texto
def descriptografar(let1, let2, m,dict):
    pos1=dict[let1]
    pos2=dict[let2]
    temp=''
    if pos1[0] == pos2[0]:
        temp+=m[pos1[0]][(pos1[1]-1)%5]
        temp+=m[pos2[0]][(pos2[1]-1)%5]
    elif pos1[1] == pos2[1]:
        temp+=m[(pos1[0]-1)%5][pos1[1]]
        temp+=m[(pos2[0]-1)%5][pos2[1]]
    else:
        temp+=m[pos1[0]][pos2[1]]
        temp+=m[pos2[0]][pos1[1]]
    return temp

#Analisa se o texto esta pronto, se não, o prepara para a criptografia
def prepararTexto(palavra):
    precript=''
    i=0
    maximo=len(palavra)-2
    while(maximo >= i):
        if palavra[i] != palavra[i+1]:
            precript+=palavra[i]+palavra[i+1]
        else:
            if i < len(palavra)-2:
                if palavra[i] != 'x':
                    precript+=palavra[i]+'x'+palavra[i+1]+palavra[i+2]
                    i+=1
                else:
                    precript+=palavra[i]+'z'+palavra[i+1]+palavra[i+2]
                    i+=1
            else:
                if palavra[i] != 'x':
                    precript+=palavra[i]+'x'+palavra[i+1]
                    i+=1
                else:
                    precript+=palavra[i]+'z'+palavra[i+1]
                    i+=1
        if i+2 == len(palavra)-1:
            precript+=palavra[i+2]
        i+=2
    return precript

#Após descriptografar remover caracteres inseridos para realizar a criptografia
def removerXZ(texto,teste):
    novoTexto=''
    for i in range(1, len(texto),2):
        if i < len(texto)-1:
            if texto[i] == 'x' or texto[i] == 'z':
                if texto[i-1] == texto[i+1]:
                    novoTexto+=texto[i-1]
                else:
                    novoTexto+=texto[i-1]+texto[i]
            else:
                novoTexto+=texto[i-1]+texto[i]
        else:
            if ultimo:
                novoTexto+=texto[i-1]
            else:
                novoTexto+=texto[i-1]+texto[i]
    return novoTexto

cript=''
precript=''
poscript=''
a=[]
ultimo=False
mapa={}
alfabeto=["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","w","v","x","y","z"]

while (True):
    print('---------- Cyfra de Playfair ----------')
    print('1 - Criptografar')
    print('2 - Descriptografar')
    print('0 - Sair')
    op=int(input())
    if ( op == 0 ):
        print("Fechando Programa!!")
        break
    chave=input("Informe a chave de segurança: ").lower().replace("ç","c").replace("k","c")
    tam=len(chave)
    if( op == 1 ):
        texto=input("Informe um texto: ").lower().replace(" ","").replace("ç","c").replace("k","c")
        arq = open('criptografia.txt', 'w')
        for i in range(0, tam):
            a.append(chave[i])

        for i in alfabeto:
            a.append(i)

        a=removerRepeticoes(a)
        m = montarMatriz(a)
        mapa=mapear(m)

        for i in m:
            print(i)

        precript=prepararTexto(texto)

        if len(precript)%2 != 0:
            ultimo=True
            if precript[len(precript)-1] != 'x':
                precript+='x'
            else:
                precript+='z'
        else:
            ultimo=False
        
        for i in range(0,len(precript), 2):
            cript+=criptografar(precript[i],precript[i+1],m,mapa)

        texto = []
        texto.append(cript+'\n')
        texto.append(str(ultimo))
        print("Este é o criptografado: "+cript)
        arq.writelines(texto)
        arq.close()
        input("Pressione Enter para continuar")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif ( op == 2 ):
        try:
            arq = open('criptografia.txt', 'r')
            texto=arq.read().split('\n')
        except Exception:
            print("Arquivo Inexistente!!")
            input("Pressione Enter para continuar")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        for i in range(0, tam):
            a.append(chave[i])

        for i in alfabeto:
            a.append(i)

        a=removerRepeticoes(a)
        m=montarMatriz(a)
        mapa=mapear(m)

        for i in m:
            print(i)

        cript=texto[0]
        print(poscript)
        for i in range(0,len(cript),2):
            poscript+=descriptografar(cript[i],cript[i+1],m,mapa)
        poscript=removerXZ(poscript,bool(texto[1]))
        arq.close()
        print("Texto Descriptografado: "+poscript)
        input("Pressione Enter para continuar")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Opção Invalida")
        input("Pressione Enter para continuar")
        os.system('cls' if os.name == 'nt' else 'clear')
