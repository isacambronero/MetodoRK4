#!/usr/bin/env python3

def dyn_generator(oper, state):
    """Genera el operador dinámico mediante la multiplicación de las matrices, se resta la misma operación en el orden opuesto. Se multiplica el resultado por -1.0j.

    Examples:
       >>> dyn_generator(np.array( [[0,1], [1,0]] ), np.array( [[1,0], [0,0]] )):
       [ [0  1.0j ] 
       [-1.0j  0 ] ]

    Args:
       oper (ndarray): primera matriz (operador)
       state (ndarray): segunda matriz (estado inicial)

    Returns: 
       ndarray: Devuelve el operador dinámico que se calculó.
    """

    return -1.0j*(np.dot(oper, state)-np.dot(state, oper))

def rk4(func, oper, state, h):
    """Implementación del método RK4. 
    
    Examples:
       >>> rk4(dyn_generator, np.array( [[0,1 ], [1,0]]), np.array( [[1,0], [0,0]] ), 0.1)
       [[0.9556341+0.j        0.       +0.2059047j]
       [0.       -0.2059047j 0.0443659+0.j       ]]

    Args:
       func (function): función que genera el operador dinámico y recibe dos parámetros
       oper (ndarray): operador, es una matriz que se pasa como parámetro a la función anterior `func`
       state (ndarray): es el estado inicial o actual, la segunda matriz que es parámetro de la función `func` 
       h (float): el intervalo entre una entrada del arreglo de valores temporales homogéneos y la anterior a ella. 

    Returns:
       ndarray: nuevo estado ($Y_{n+1})$  después de utilizar el método.
    """

    k_1 = h*func(oper, state)
    k_2 = h*func(oper + h/2, state + k_1/2)
    k_3 = h*func(oper + h/2, state + k_2/2)
    k_4 = h*func(oper + h, state + k_3)
    return state + (1/6)*(k_1+2*k_2+2*k_3+k_4)













