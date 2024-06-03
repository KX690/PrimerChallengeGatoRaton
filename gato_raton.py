import random
import time

cuadricula = int(input("Introduzca el tamaño de la cuadricula: "))
moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]


raton = [0, 0]
gato = [cuadricula - 1, cuadricula - 1]

def render_tabla():
    tabla = [['.' for _ in range(cuadricula)] for _ in range(cuadricula)]
    tabla[raton[0]][raton[1]] = "R"
    tabla[gato[0]][gato[1]] = "G"

    for fila in tabla:
        print(" ".join(fila))
    print("**********************************************")

def calcular_distancia(raton, gato):
    return abs(raton[0] - gato[0]) + abs(raton[1] - gato[1])

def evaluate(position):
    raton, gato = position
    return calcular_distancia(raton, gato)

def get_children(position, jugada_a_maximizar):
    raton, gato = position
    children = []
    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    if jugada_a_maximizar:
        for move in moves:
            new_raton = [raton[0] + move[0], raton[1] + move[1]]
            if 0 <= new_raton[0] < cuadricula and 0 <= new_raton[1] < cuadricula:
                children.append((new_raton, gato))
    else:
        for move in moves:
            new_gato = [gato[0] + move[0], gato[1] + move[1]]
            if 0 <= new_gato[0] < cuadricula and 0 <= new_gato[1] < cuadricula:
                children.append((raton, new_gato))

    return children

def minimax(position, depth, jugada_a_maximizar):
    if depth == 0 or position[0] == position[1]:                                        #En este punto donde la posicion del raton y del gato son iguales termina el juego
        return evaluate(position)

    if jugada_a_maximizar:
        max_valor = float('-inf')
        for child in get_children(position, jugada_a_maximizar):
            valor = minimax(child, depth - 1, False)
            max_valor = max(max_valor, valor)
        return max_valor
    else:
        min_valor = float('inf')
        for child in get_children(position, jugada_a_maximizar):
            valor = minimax(child, depth - 1, True)
            min_valor = min(min_valor, valor)
        return min_valor

def mueve_gato():
    global gato, raton

    
    if raton[0] == gato[0] or raton[1] == gato[1]:                                      #Verificamos si el gato y el raton estan alineados
        if raton[0] == gato[0]:                                                         #Si esta alineado horizontalmente se acerca al raton de forma directa
            if raton[1] < gato[1]:
                gato[1] -= 1
            else:
                gato[1] += 1
        elif raton[1] == gato[1]:                                                       #Lo mismo que ocurre si estan horizontal pero ahora vertical
            if raton[0] < gato[0]:
                gato[0] -= 1
            else:
                gato[0] += 1
    else:
        mejor_movimiento = None
        mejor_valor = float('inf')
        for child in get_children((raton, gato), False):
            valor = minimax(child, 3, True)                                             #Le di 3 niveles de profundidad para el minimax, esto puede ser cambiado
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimiento = child
        gato = mejor_movimiento[1]

def mueve_raton():                                                                      #Juega el raton, para evitar problemas le espesifico nuevamente que raton y gato son variables globales
    global raton, gato
    mejor_movimiento = None
    mejor_valor = float('-inf')
    for child in get_children((raton, gato), True):                                     #Paso las posiciones del gato y el raton como tupla
        valor = minimax(child, 3, False)  
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = child
    raton = mejor_movimiento[0]

render_tabla()
mueve_raton()
numero=random.randrange(1,2)
match numero:
    case 1: 
        raton+=moves[1]
    case 2:
        raton+=moves[2]

time.sleep(2)
render_tabla()

while raton != gato:
    time.sleep(2)
    mueve_gato()
    render_tabla()

    if raton == gato:
        print("Gano el gato")
        break

    time.sleep(2)
    mueve_raton()
    render_tabla()