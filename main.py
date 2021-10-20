def citire_lista1():
    lista = []
    string_lista = input('Dati elementele multimii A, separate printr-un spatiu: ')
    string_elemente = string_lista.split(sep=' ')
    for string_element in string_elemente:
        element = int(string_element)
        lista.append(element)
    return lista


def citire_lista2():
    lista = []
    string_lista = input('Dati elementele multimii B, separate printr-un spatiu: ')
    string_elemente = string_lista.split(sep=' ')
    for string_element in string_elemente:
        element = int(string_element)
        lista.append(element)
    return lista


def citire_lista3():
    lista = []
    string_lista = input('Dati elementele multimii C, separate printr-un spatiu: ')
    string_elemente = string_lista.split(sep=' ')
    for string_element in string_elemente:
        element = int(string_element)
        lista.append(element)
    return lista


def lista_pare(lista):
    """
    Creeaza o lista doar cu numerele pare dintr-o lista principala
    :param lista: lista principala
    :return: lista formata doar din numerele pare din lista principala
    """
    rezultat = []
    for element in lista:
        if element % 2 == 0:
            rezultat.append(element)
    return rezultat


def test_lista_pare():
    assert lista_pare([1, 2, 4, 6,7]) == [2, 4, 6]
    assert lista_pare([5, 7, 9, 11]) == []
    assert lista_pare([-2, 4, 6, 31]) == [-2, 4, 6]


test_lista_pare()


def acelasi_numar_pare(lista1, lista2):
    """
    Verifica daca numarul de elemente pare dintr-o lista este egal cu numarul de elemente pare din alta lista
    :param lista1: prima lista
    :param lista2: a doua lista
    :return: True - daca nr. elem. pare din lista1 este egal cu nr. elem. pare din lista2
             False - daca nr. elem. pare din lista1 nu este egal cu nr. elem. pare din lista2
    """
    lista_pare1 = lista_pare(lista1)
    lista_pare2 = lista_pare(lista2)
    if len(lista_pare1) == len(lista_pare2):
        return True
    else:
        return False



def test_acelasi_numar_pare():
    assert acelasi_numar_pare([1, 2, 5], [2, 3]) is True
    assert acelasi_numar_pare([7, 6, 4, 2], [1, 3]) is False
    assert acelasi_numar_pare([7], [3]) is True


test_acelasi_numar_pare()


def element_inclus(element, lista):
    """
    Verifica daca un numar element apare intr-o lista
    :param element: numarul despre care vrem sa stim daca apare in lista
    :param lista: lista
    :return: True - daca element este in lista
             False - daca element nu este in lista
    """
    for numar in lista:
        if element == numar:
            return True
    return False


def test_element_inclus():
    assert element_inclus(10, [10, 12, 89]) is True
    assert element_inclus(9, [3, 48, 109, 7]) is False


test_element_inclus()


def intersectie(lista1, lista2):
    """
    Creeaza o lista formata prin intersectia a doua liste
    :param lista1: prima lista
    :param lista2: a doua lista
    :return: rezultatul intersectiei dintre lista1 si lista2
    """
    rezultat = []
    for element in lista1:
        if element_inclus(element, lista2) is True:
            rezultat.append(element)
    return rezultat


def test_intersectie():
    assert intersectie([1, 2, 3, 5], [1, 6, 2]) == [1, 2]
    assert intersectie([1, 2, 3, 5], [4, 6, 8]) == []
    assert intersectie([-7, -8, 3, 6], [4, 6, -8]) == [-8, 6]


test_intersectie()


def concatenare_elemente(element1, element2):
    """
    Concateneaza doua numere. Daca primele cifre din primul numar sunt 0, acestea nu se vor lua
     in considerare
    :param element1: primul element pozitiv
    :param element2: al doilea element pozitiv
    :return: concatenarea element1 cu element2
    """
    rezultat = str(element1) + str(element2)
    return int(rezultat)


def test_concatenare():
    assert concatenare_elemente(0, 14) == 14
    assert concatenare_elemente(78, 84) == 7884
    assert concatenare_elemente(5, 0) == 50


test_concatenare()


def is_palindrom(n):
    """
    Verifica daca un numar dat este palindrom
    :param n: numarul natural pe care vrem sa il verificam
    :return: True - daca n este palindrom
             False - daca n nu este palindrom
    """
    n = str(n)
    oglindit = n[::-1]
    if n == oglindit:
        return True
    else:
        return False


def test_is_palindrom():
    assert is_palindrom(14541) is True
    assert is_palindrom(4753) is False
    assert is_palindrom((5)) is True


test_is_palindrom()


def elemente_concatenate_palindrom(lista1, lista2):
    rezultat = []
    if len(lista1) < len(lista2):
        dimensiune = len(lista1)
    else:
        dimensiune = len(lista2)
    for pozitie in range(dimensiune):
        nr_concatenat = concatenare_elemente(lista1[pozitie], lista2[pozitie])
        if is_palindrom(nr_concatenat):
            rezultat.append(nr_concatenat)
    return rezultat


def test_elemente_concatenate_palindrom():
    assert elemente_concatenate_palindrom([12, 22, 36, 11], [21, 23, 63, 55, 424]) == [1221, 3663]
    assert elemente_concatenate_palindrom([7, 0, 11], [7, 5, 23, 63, 55]) == [77, 5]


test_elemente_concatenate_palindrom()


def divizibil_k(n, k):
    """
    Verifica daca un numar n este divizibil cu un numar k
    :param n: numarul intreg pentru care vrem sa vedem daca k ii e divizor
    :param k: nuar intreg, diferit de 0, care vrem sa vedem daca e divizor a lui n
    :return: True - daca n divizibil cu k
             False - daca n nu e divizibil cu k
    """
    if n % k == 0:
        return True
    else:
        return False


def test_divizibil_k():
    assert divizibil_k(7, 8) is False
    assert divizibil_k(-10, 2) is True
    assert divizibil_k(5, 1) is True
    assert divizibil_k(0, 25) is True
    assert divizibil_k(100, -20) is True


test_divizibil_k()


def oglindit(numar):
    """
    Determina oglinditul unui numar pozitiv. Daca numarul se termina cu unul sau mai multe elemente 0, nu vor
    aparea in oglindit
    :param numar: numarul
    :return: oglinditul lui numar
    """
    numar_str = str(numar)
    oglindit = numar_str[::-1]
    return int(oglindit)


def test_oglindit():
    assert oglindit(78) == 87
    assert oglindit(400) == 4

test_oglindit()


def modificare_lista(lista1, lista2):
    """
    Modifica o lista penrtru care elementele care sunt divizibile cu toate elemente din a doua lista, se inlocuiesc cu
    oglinditul lor
    :param lista1: prima lista
    :param lista2: a doua lista
    :return: rezultat - lista in care elementele din lista1 sunt inlocuite cu oglinditul lor daca elementul este
    divizibil cu toate elementele din lista2. Daca nu exista astfel de elemente, rezultat ramane lista1
    """
    rezultat = []
    for element1 in lista1:
        ok = True
        for element2 in lista2:
            if divizibil_k(element1, element2) is False:
                ok = False
        if ok is not True:
            rezultat.append(element1)
        else:
            rezultat.append(oglindit(element1))
    return rezultat


def test_modificare_lista():
    assert modificare_lista([24, 40, 62, 7], [2]) == [42, 4, 26, 7]
    assert modificare_lista([12, 22, 36, 363], [1, 2, 3, 4]) == [21, 22, 63, 363]
    assert modificare_lista([22, 23, 36, 55, 363], [1, 2, 3, 4]) == [22, 23, 63, 55, 363]


test_modificare_lista()


def main():
    A = []
    B = []
    while True:
        print('1. Citirea a două mulțimi de numere întregi de la tastatura sub forma a două liste.')
        print('2. Afișați dacă cele două liste au același număr de elemente pare.')
        print('3. Afișați o listă reprezentând intersecția listelor citite de la tastatură.')
        print('4. Afișați toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în '
              'cele două liste.')
        print('5. Se citeste o a treia listă și afișați listele obținute prin înlocuirea în cele două liste citite '
              'la punctul 1 a tuturor elementelor cu oglinditul lor dacă îndeplinesc următoarea regulă: elementele'
              ' sunt divizibile cu toate elementele din a treia lista. Dacă nu îndeplinesc regula, păstrați elementul'
              ' așa cum e.')
        print('6.Exit')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            A = citire_lista1()
            B = citire_lista2()
            print(A)
            print(B)
        elif optiune == '2':
            print(acelasi_numar_pare(A, B))
        elif optiune == '3':
            print(intersectie(A, B))
        elif optiune == '4':
            print(elemente_concatenate_palindrom(A, B))
        elif optiune == '5':
            C = citire_lista3()
            listaA = modificare_lista(A, C)
            listaB = modificare_lista(B, C)
            print(listaA, ' si ', listaB)
        elif optiune == '6':
            break
        else:
            print('optiune invalida')

main()