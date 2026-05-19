    # Replace the "ANSWER HERE" for your answer

def enumerate_list(lst):
    """
    Dada una lista de strings, retorna una nueva lista donde cada elemento
    tiene el formato "indice. valor". Los strings vacios se deben saltear
    y no deben aparecer en la lista resultante.
    El indice debe ser consecutivo (no el indice original).

    Ejemplo: enumerate_list(["Red", "Green", "", "White"]) -> ["0. Red", "1. Green", "2. White"]
    """
    lista_new = []
    indice = 0
    for n in lst:
        if n.strip() != "":
            lista_new.append(f"{indice}. {n}")
            indice +=1
    return lista_new



def enumerate_backwards(lst):
    """
    Igual que enumerate_list, pero cada palabra debe estar escrita al reves.
    Los strings vacios se deben saltear.

    Ejemplo: enumerate_backwards(["Red", "Green", ""]) -> ["0. deR", "1. neerG"]
    """
    lista_new = []
    indice = 0
    for n in lst:
        if n.strip() != "":
            lista_new.append(f"{indice}. {n[::-1]}")
            indice +=1
    return lista_new
