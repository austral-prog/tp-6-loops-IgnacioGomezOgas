# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lst=[]
    for sublista in matrix:
        lst=lst+sublista
    return lst



def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    lst=[]
    for sublista in matrix:
        lst.append(sum(sublista))
    return lst


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    if not matrix:
        return []
    lst=[]
    cantidad_col=len(matrix[0])
    for c in range(cantidad_col):
        suma_actual=0
        for fila in matrix:
            suma_actual=suma_actual+fila[c]
        lst.append(suma_actual)
    return lst


