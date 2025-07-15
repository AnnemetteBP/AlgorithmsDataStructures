from Element import Element

""" Da denne del er fra projekt del I, er kommentarer fjernet.
    I stedet for, at e og min er integers, er de nu typebestemte som Element.
    I Del III af projektet, benyttes dette modul til at finde de to mindste knuder.
    De to mindste knuder merges først for derved at opnå det længste kodeord.
    Det vil man fordi, at de mindst hyppige karakterer skal have tildelt de længste kodeord. """

def extractMin(A:list[Element]) -> Element: 
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0] 
    min = A.pop() 
    heapify(A, 0) 
    
    return min 


def insert(A:list, e:Element) -> None:   
    A.append(e) 
    i = len(A) - 1 

    while i > 0 and A[parent(i)] > A[i]: 
        A[i], A[parent(i)] = A[parent(i)], A[i] 
        i = parent(i)


def createEmptyPQ() -> list:    
    return []


def left(i:int) -> int:
    return 2*i + 1

def right(i:int) -> int:
    return 2*i + 2

def parent(i:int) -> int:
    return (i - 1)//2


def heapify(A:list, i:int) -> None:
    smallest = i 
    l = left(i) 
    r = right(i) 
    
    if l >= 0 and l < len(A) and A[l] < A[i]:  
        smallest = l 
    else:
        smallest = i 

    if r >= 0 and r < len(A) and A[r] < A[smallest]:
        smallest = r 

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i] 
        heapify(A, smallest)