""" DETALJER:

        Gruppe:
             SDU-logins:
                Navn: Annemette Brok Pirchert
                Mail: anpir23@student.sdu.dk

        Beskrivelse:
            Python implementation HEAP-SORT på binært MIN-HEAP.
            Modsat MAX-HEAP, hvor A[Parent(i)] >= A[i] da ser man, at det for MIN-HEAP gælder A[Parent(i)] <= A[i].
            Dvs. at A[Parent(i)] <= A[i] er den heap property som må overholdes og vedligholdes af HEAPIFY Proceduren.
            Både den samlede og worst-case samt average-case/expected køretid for HEAP-SORT er O(n lg n). 
           
            Version: Python 3.11.5
            Installs / Imports: None
            Testet med alle filerne i "Testfiler" på Windows via PowerShell terminalen
            * Alle side referencer må betragtes ift. Cormen (4 udgave) et al. kapitel 6.

        Test eksempel med PowerShell (input: < increasing.tx > output: PQSort.py):
            >> CMD: Get-Content .\Testfiler\Testfiler\increasing.txt | python .\PQSort.py """


""" ====== START: PSEUDOKODE SIDE 175 (MAX-HEAP-EXTRACT-MAX) ====== """

def extractMin(A:list) -> int:
    """ Fjern elementet med mindst prioritet fra prioritetskøen A og returner det.
        
        extractMin(A) inputkontrol er overladt til brugeren af prioritetskøen.
        heapify proceduren kaldes med argumenterne A og 0.
        Til forskel fra bogens pseudokode, kaldes heapify med argumentet 0 i stedet for 1.
        Ovenstående ændring er for at respektere den Pythoniske måde hvorpå liste-objekter indekseres.
        For INSERT gælder det at A = A U {x} og for EXTRACT-MIN retunerer man elementet x i A med mindste key.
        min / roden assignes til det sidste element i A (A[-1]) med A.pop() og man får som følge A[0:n-1]. """
    
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0] 
    min = A.pop() 
    heapify(A, 0) 
    return min 

""" ====== SLUT: PSEUDOKODE SIDE 175 ====== """


""" ====== START: PSEUDOKODE SIDE 176 (MAX-HEAP-I NCREASE-KEY og MAX-HEAP-INSERT) ====== """

def insert(A:list, e:int) -> None:
    """ Indsæt elementet e i prioritetskøen A.
        
        Sammenskrivning af pseudokode side 176 i følge med opgavebeskrivelsen.
        insert kaldes fra PQSort modulet og insætter linjer fra input filen i prioritetskøen.
        prioritetskøen er her A, som der i PQSort modulet refereres til som pq. """
    
    A.append(e) 
    i = len(A) - 1 

    while i > 0 and A[parent(i)] > A[i]: 
        A[i], A[parent(i)] = A[parent(i)], A[i] 
        i = parent(i) 

    """ Udkommenter nedenstående så printHeap() kaldes med A som argument for at observere heapify. """
    #printHeap(A)

""" ====== SLUT: PSEUDOKODE SIDE 176 ====== """


""" ====== START: createEmptyPQ ====== """

def createEmptyPQ() -> list:
    """ Returner en ny, tom prioritetskø (dvs. en tom liste).
        createEmptyPQ kaldes fra PQSort modulet og opretter en tom prioritetskø ved navn pq. """
    
    return []

""" ====== SLUT: createEmptyPQ ====== """


""" ====== START: PSEUDOKODE SIDE 162 (Den (binære) heap datastruktur) ====== """

def left(i:int) -> int:
    """ Retunerer: Left(i) = 2i + 1 hvor i er et element i listen A. """
    return 2*i + 1

def right(i:int) -> int:
    """ Retunerer: Right(i) = 2i + 2 hvor i er et element i listen A. """
    return 2*i + 2

def parent(i:int) -> int:
    """ Retunerer: Parent(i) = ⌊(i − 1)/2⌋ hvor i er et element i listen A. """
    return (i - 1)//2

""" ====== SLUT: PSEUDOKODE SIDE 162 ====== """


""" ====== START: PSEUDOKODE SIDE 165 (MAX-HEAPIFY) ====== """

def heapify(A:list, i:int) -> None:
    """ MAX/MIN-HEAPIFY Proceduren:
            Vedligeholder rekursivt en given heap property.
            Elementer ombyttes så min-heap property overholdes.
            Hér A[Parent(i)] <= A[i].
            Hvert n-1 kald af heapify tager O(lg n) tid.
        
        Følgende scenarier håndteres:

            1: Hvis venstre barn ikke er et blad, eller mindre end sin forældre:
                så swap og ellers er smallest forældren.

            2: Hvis højre barn ikke er et blad, eller mindre end sin forældre:
                så swap de to.

            3: Hvis smallest ikke er lig med forældren:
                swap da og kald sig selv rekursivt for at vedligeholde min-heap property. """
    
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

""" ====== SLUT: PSEUDOKODE SIDE 165 ====== """


""" ====== PRINT HEAP FUNKTION ====== """

def printHeap(heap:list) -> None:
    """ Print heap strukturen i pyramideform for at observere hvordan HEAP-SORT udvikler sig.
        Kaldes i insert funktionen hvis udkommenteres. Dvs. #printHeap(A) => printHeap(A). """
    
    print("------HEAP START------")
    level:int = 0
    nodes_on_level:int = 1
    current_node:int = 0

    while current_node < len(heap):
        for _ in range(nodes_on_level):
            print(f"{heap[current_node]:^4}", end=" ")
            current_node += 1
            if current_node >= len(heap):
                break

        print() 

        level += 1
        nodes_on_level *= 2

    print("------HEAP END------")  