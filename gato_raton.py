import random
import time

cuadricula = int(input("Introduzca el tamaño de la cuadricula: "))

norte=[0,-1]
sur=[0,1]
este=[1,0]
oeste=[-1,0]

distancia_raton=[0]*4
distancias_gato=[0]*4
posible_norte=[]
posible_sur=[]
posible_este=[]
posible_oesto=[]

raton= [0,0]
raton_futuro=[0,0]
gato_futuro=[3,3]

gato=[cuadricula-1,cuadricula-1]
b=True

def render_tabla():
    tabla = [[0 for _ in range(cuadricula)] for _ in range(cuadricula)]

    for i in range(cuadricula):
        for j in range(cuadricula):
            tabla[i][j]="."


    tabla[raton[0]][raton[1]]="R"
    tabla[gato[0]][gato[1]]="G"


    for i in range(cuadricula):
        
        for j in range(cuadricula):
            print(f"{tabla[i][j]} ", end='')
        
        print("\n")
        
    print("**********************************************")

def calcular_distancia(posible):
    #se movio al norte mi gato
    distancia=(abs(posible[0]-gato[0])+abs(posible[1]-(gato[1])))

    return distancia  
  

def calcular_distancia_futuro(posible_gato):
    
    distancia=((abs(posible_gato[0]-raton_futuro[0])+abs(posible_gato[1]-(raton_futuro[1])))+(abs(posible_gato[0]-raton[0])+abs(posible_gato[1]-raton[1])))
    if(posible_gato[0]==posible_gato[1]):
        return (distancia - 1)
    return distancia
render_tabla()

    
    

def mueve_gato():
    global gato, raton_futuro
    
    raton_futuro=[raton[0],raton[1]]
    #Para los movimientos le puse como restriccion los limites del rablero
    #Norte
    if(raton[0]>0):
        posible_norte=[raton[0]-1,raton[1]]
        distancia_raton[0]=calcular_distancia(posible_norte)
    else:
        distancia_raton[0]=0
    #Sur
    if(raton[0]<cuadricula-1):
        posible_sur=[raton[0]+1, raton[1]]
        distancia_raton[1]=calcular_distancia(posible_sur)
    else:
        distancia_raton[1]=0
            
    #Este
    if(raton[1]<cuadricula-1):
        posible_este=[raton[0],raton[1]+1]
        distancia_raton[2]=calcular_distancia(posible_este)
    else:
        distancia_raton[2]=0
        
    #Oeste
    if(raton[1]>0):
        posible_oeste=[raton[0], raton[1]-1]
        distancia_raton[3]=calcular_distancia(posible_oeste)
    else:
        distancia_raton[3]=0
        
    #Guardo las distancias a todos los posibles valores de movimiento del raton
    valor_maximo = max(distancia_raton)
    #Como estan guardados en orden, el indice indica hacia que movimiento tiene la mayor distancia
    valor_index = distancia_raton.index(valor_maximo)
    
    #Tomando el indice elegimos que movimiento posiblemente haga el raton
    match valor_index:
            case 0:
                raton_futuro[0]=raton_futuro[0]+norte[1]           
                raton_futuro[1]=raton_futuro[1]+norte[0]  
            case 1:
                raton_futuro[0]=raton_futuro[0]+sur[1]
                raton_futuro[1]=raton_futuro[1]+sur[0]
            case 2:
                raton_futuro[0]=raton_futuro[0]+este[1]
                raton_futuro[1]=raton_futuro[1]+este[0]
            case 3:
                raton_futuro[0]=raton_futuro[0]+oeste[1]
                raton_futuro[1]=raton_futuro[1]+oeste[0]
    #Comienza a pensar su movimiento el gato
    #Si la distancia al raton es 1 directamente se movera al lugar del raton
    #Pero si el raton esta mas alejado, el pensara que camino le combiene
    if(calcular_distancia(raton)!=1):
        
        #Norte
        if(gato[0]>0):
            posible_norte=[gato[0]-1,gato[1]]
            distancias_gato[0]=calcular_distancia_futuro(posible_norte)
        else:
            distancias_gato[0]=cuadricula*cuadricula
        #Sur
        if(gato[0]<cuadricula-1):
            posible_sur=[gato[0]+1, gato[1]]
            distancias_gato[1]=calcular_distancia_futuro(posible_sur)
        else:
            distancias_gato[1]=cuadricula*cuadricula
                
        #Este
        if(gato[1]<cuadricula-1):
            posible_este=[gato[0],gato[1]+1]
            distancias_gato[2]=calcular_distancia_futuro(posible_este)
        else:
            distancias_gato[2]=cuadricula*cuadricula
            
        #Oeste
        if(gato[1]>0):
            posible_oeste=[gato[0], gato[1]-1]
            distancias_gato[3]=calcular_distancia_futuro(posible_oeste)
        else:
            distancias_gato[3]=cuadricula*cuadricula
            
        #Guardamos los valores minimos
        valor_minimo = min(distancias_gato)
        #Elegimos el indice de la distancia menor a los posibles valores del raton
        valor_index = distancias_gato.index(valor_minimo)
        
        #Le pasamos el indice para que realice el movimiento el gato
        match valor_index:
            case 0:
                gato[0]=gato[0]+norte[1]
                gato[1]=gato[1]+norte[0]
            case 1:
                gato[0]=gato[0]+sur[1]
                gato[1]=gato[1]+sur[0]
            case 2:
                gato[0]=gato[0]+este[1]
                gato[1]=gato[1]+este[0]
            case 3:
                gato[0]=gato[0]+oeste[1]
                gato[1]=gato[1]+oeste[0]
    else:
        #Si la distancia era 1 significa que estaba alado, por lo tanto ya atrapa al raton
        gato=[raton[0],raton[1]]
  


def mueve_raton():
    gato_futuro=[gato[0],gato[1]]
    
    if(gato[0]>0):
        posible_norte=[gato[0]-1,gato[1]]
        distancias_gato[0]=calcular_distancia(posible_norte)
    else:
        distancias_gato[0]=0
        
        
    if(gato[0]<cuadricula-1):
        posible_sur=[gato[0]+1, gato[1]]
        distancias_gato[1]=calcular_distancia(posible_sur)
    else:
        distancias_gato[1]=0
            
        
    if(gato[1]<cuadricula-1):
        posible_este=[gato[0],gato[1]+1]
        distancias_gato[2]=calcular_distancia(posible_este)
    else:
        distancias_gato[2]=0
        
       
    if(gato[1]>0):
        posible_oeste=[gato[0], gato[1]-1]
        distancias_gato[3]=calcular_distancia(posible_oeste)
    else:
        distancias_gato[3]=0
        
        
    valor_maximo = max(distancias_gato)
    valor_index = distancias_gato.index(valor_maximo)
    
    
    match valor_index:
            case 0:
                gato_futuro[0]=gato_futuro[0]+norte[1]           
                gato_futuro[1]=gato_futuro[1]+norte[0]  
            case 1:
                gato_futuro[0]=gato_futuro[0]+sur[1]
                gato_futuro[1]=gato_futuro[1]+sur[0]
            case 2:
                gato_futuro[0]=gato_futuro[0]+este[1]
                gato_futuro[1]=gato_futuro[1]+este[0]
            case 3:
                gato_futuro[0]=gato_futuro[0]+oeste[1]
                gato_futuro[1]=gato_futuro[1]+oeste[0]

    
    if(raton[0]>0):
        posible_norte=[raton[0]-1,raton[1]]
        distancia_raton[0]=calcular_distancia_futuro(posible_norte)
    else:
        distancia_raton[0]=cuadricula*cuadricula
        
    if(raton[0]<cuadricula-1):
        posible_sur=[raton[0]+1, raton[1]]
        distancia_raton[1]=calcular_distancia_futuro(posible_sur)
    else:
        distancia_raton[1]=cuadricula*cuadricula
            
        
    if(raton[1]<cuadricula-1):
        posible_este=[raton[0],raton[1]+1]
        distancia_raton[2]=calcular_distancia_futuro(posible_este)
    else:
        distancia_raton[2]=cuadricula*cuadricula
        
       
    if(raton[1]>0):
        posible_oeste=[raton[0], raton[1]-1]
        distancia_raton[3]=calcular_distancia_futuro(posible_oeste)
    else:
        distancia_raton[3]=cuadricula*cuadricula
        
    
    valor_minimo = min(distancia_raton)
    valor_index=distancia_raton.index(valor_minimo)
    
    
    match valor_index:
        case 0:
            raton[0]=raton[0]+norte[1]
            raton[1]=raton[1]+norte[0]
        case 1:
            raton[0]=raton[0]+sur[1]
            raton[1]=raton[1]+sur[0]
        case 2:
            raton[0]=raton[0]+este[1]
            raton[1]=raton[1]+este[0]
        case 3:
            raton[0]=raton[0]+oeste[1]
            raton[1]=raton[1]+oeste[0]
        

        

render_tabla()   
mueve_raton()
time.sleep(2)
render_tabla()   
while(raton!=gato):
    time.sleep(2)
    mueve_gato()
    render_tabla()
    
    if(raton==gato):
        print("Gano el gato")
        break
    time.sleep(2)
    mueve_raton()
    render_tabla()
   