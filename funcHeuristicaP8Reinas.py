
#    Análisis y diseño de algoritmos
#    Vivar Olvera Marco Antonio


#    "funcion heuristica al problema de las 8 reinas"
#    (Implementar la funcion heuristica que cuenta casillas no atacadas)
#    entrega: 30/01/22

#representacion de estados
# 0:disponible
# 1:bloqueada
# 2:ocupada

import copy

def bloqCasilla(t,f): #se le pasa a la funcion por referencia una matriz
    posicionarReina(t,f)    #se le llama al metodo para posicionar reina y asi poder bloquear las casillas en este metodo
    #se bloquea la fila en donde esta posicionada la reina
    for i in range(N):
        if(t[f][i]!=2):
            t[f][i]=1
    #si la fila pasada a la funcion es la ultima se saldra de esta  
    if(f==N-1):
        return f
    #se bloquea las casillas que ataca la reina posicionada(2)
    for i in range(N):
        if(t[f][i]==2):
            #se valida que no sea una casilla del borde inferior
            if(f!=N-1):
                for j in range(f+1,N):  #bloque de la vertical
                    t[j][i]=1  
            #se valida que no sea una casilla del borde derecho
            if(i!=N-1):
                k=f+1
                for j in range(i+1,N):  #bloqueo diagonal derecha
                    t[k][j]=1
                    k=k+1
                    if(k==N):
                        break
            #se valida que no sea una casilla del borde izquierdo
            if(i!=0):
                k=f+1
                for j in range(i-1,-1,-1):  #bloqueo diagonal izquierda
                    t[k][j]=1
                    k=k+1 
                    if(k==N):
                        break   
            break   #una vez encontrada la reina de la fila se sale del for
    
    #se imprime la matriz fila por fila*********DEMUESTRA LOS CAMBIOS
    for i in range(N):
        print(tablero[i])
    print()
    #********************************************
    return bloqCasilla(t,f+1) #se vuelve a llamar al metodo *****


#se posciona la reina en la casilla con la regla de mayor peso  
def posicionarReina(t,f):
    if(f==0):
        tablero[0][N//2]=2  #SE POSICIONA LA PRIMERA REINA EN LA PRIMERA FILA (PODEMOS ELEGIR LA COLUMNA)
        return
    #SE APLICA LA PRIMERA REGLA en las casillas disponibles, si hay una que cumple es el fin de la funcion     
    for i in range(N):
        if(t[f][i]==0):
            if(movCaballo(t,f,i)==True):
                t[f][i]=2
                return           
    #si no se encontro una casilla con el criterio anterior, SE IMPLEMENTA LA SEGUNDA REGLA
    mejorCasilla=[] #se va a guardar el indice y el numero de casillas no atacadas, 
    max=-1
    for i in range(N):  #se itera para encontrar el valor mas grande de casillas que ofrece una casilla candidat 
        if(t[f][i]==0):
            
            if(contaCasillasNoAtac(t,f,i)>max):
                max=contaCasillasNoAtac(t,f,i)
    for i in range(N):  #se itera para encontrar los indices con el mayor numero de casillas no atacadas con el max encontrado anteriormente  
        if(t[f][i]==0):
            #print(f,i)
            if(contaCasillasNoAtac(t,f,i)==max):
                mejorCasilla.append(i)
                
    #print(mejorCasilla)           
    if(len(mejorCasilla)==1):   #salimos del metodo ya que se encontro la casilla mejor evaluada
        t[f][mejorCasilla[0]]=2
    else:   #SE IMPLEMENTA LA TERCERA REGLA, ya que hay dos casillas o mas iguales con respecto a sus casillas no atacadas
        for x in mejorCasilla:  #recorremos la lista de los nodos mejor calificados para solo quedarnos con uno que sera el mejor calificado por el metodo
            if(filaBloqueada(t,f,i)==True):
                t[f][x]=2
                return

def movCaballo(t,f,candidata):   #principal criterio para posicionar una reina(encuentra si la casilla candidata incide en la trayectoria de movimiento de caballo con las reinas colcadadas anteriormente)
    #validamos que se pueda contar con el moviemiento completo de caballo hacia la izq-der 
    auxCandidata=candidata
    for i in range(f-1,-1,-1):
        candidata=candidata-2
        if(candidata>=0):   #puede hacer movimeinto de caballo a la izquierda
            if(t[i][candidata]==2):
                return True
        else:
            break
    for i in range(f-1,-1,-1):
        auxCandidata=auxCandidata+2
        if(auxCandidata<=N-1): #puede hacer movimeinto de caballo a la derecha
            if(t[i][auxCandidata]==2):
                return True
        else:
            break
    return False
                  

def contaCasillasNoAtac(t,f,candidata):  #segundo criterio para posicionar a traves del conteo de casillas no atacadas
    auxt=copy.deepcopy(t)   #se utiliza este metodo para no modificar la matriz original, ya que si la asignamos, lo que se esta haciendo es referenciar la original
    conta=0
    for i in range(N):
        if(i==candidata):
            #se valida que no sea una casilla del borde inferior
            if(f!=N-1):
                for j in range(f+1,N):  #bloque de la vertical
                    auxt[j][i]=1  
            #se valida que no sea una casilla del borde derecho
            if(i!=N-1):
                k=f+1
                for j in range(i+1,N):  #bloqueo diagonal derecha
                    auxt[k][j]=1
                    k=k+1
                    if(k==N):
                        break
            #se valida que no sea una casilla del borde izquierdo
            if(i!=0):
                k=f+1
                for j in range(i-1,-1,-1):  #bloqueo diagonal izquierda
                    auxt[k][j]=1
                    k=k+1 
                    if(k==N):
                        break   
            break   #una vez encontrada la reina de la fila se sale del for
    #se procede al conteo de las casillas no atacadas
    for i in range(f+1,N):
        for j in range(N):
            if(auxt[i][j]==0):
                conta=conta+1
    #print()    #prueba de funcionamiento
    #for i in range(N):
    #    print(auxt[i])
    #print(conta)
    return conta


    
    
def filaBloqueada(t,f,candidata):    #este es el ultimo recurso para posicionar una reina, verifica que no deja ninguna fila inferior sin opciones
    auxt=auxt=copy.deepcopy(t)  #se utiliza este metodo para no modificar la matriz original, ya que si la asignamos, lo que se esta haciendo es referenciar la original
    conta=0
    for i in range(N):
        if(i==candidata):
            #se valida que no sea una casilla del borde inferior
            if(f!=N-1):
                for j in range(f+1,N):  #bloque de la vertical
                    auxt[j][i]=1  
            #se valida que no sea una casilla del borde derecho
            if(i!=N-1):
                k=f+1
                for j in range(i+1,N):  #bloqueo diagonal derecha
                    auxt[k][j]=1
                    k=k+1
                    if(k==N):
                        break
            #se valida que no sea una casilla del borde izquierdo
            if(i!=0):
                k=f+1
                for j in range(i-1,-1,-1):  #bloqueo diagonal izquierda
                    auxt[k][j]=1
                    k=k+1 
                    if(k==N):
                        break   
            break   #una vez encontrada la reina de la fila se sale del for
    #se procede a verificar que la asilla candidata no deje filas inferiores bloqueadas
    for i in range(f+1,N):
        conta=0
        for j in range(N):
            if(auxt[i][j]==1):
                conta=conta+1
                if(conta==8):   #al encontrar 8 unos significa que esta toda la fila bloqueada y se descarta esa casilla candidata
                    return False
    return True #al no encontrar filas bloquedas retorna true y esa casilla es la indicada para colocar la reina




N=8 #numero de reinas
tablero=[[0 for i in range(N)]for j in range(N)]    #se crea una matriz de N*N de ceros


bloqCasilla(tablero,0)

#se imprime la matriz fila por fila
for i in range(N):
    print(tablero[i])


#PRUEBA DEL METODO DE MOVIMIENTO DE CABALLO*****************************
#tableEjem=[[0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0],
#            [2,0,0,0,0,0,0,0],
#            [0,0,1,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0]]
#print()
#for i in range(N):
#    print(tableEjem[i])
#
#print(movCaballo(tableEjem,4,2))
#************************************************************************
#PRUEBA DEL METODO DE CONTEO***********************
#contaCasillasNoAtac(tableEjem,4,4)
#**************************************************
