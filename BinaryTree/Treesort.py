import sys
from DictBinTree import DictBinTree

'''
    Gruppe:
            
    PART II: OPGAVE 2:

        Test program til DictBinTree.py, som kan køres på testfilerne fra del I.
        Importerer sys modulet samt filen DictBinTree.py som modul DictBinTree.
        Et nyt tomt DictBinTree instansieres og assignes til 'T'.
        Knude objekt(er) af typen BinNode med værdien k (hvor k er en linje fra fil) indsættes i træet (T) via T.insert().
        Resultatet af sorteringen assignes til 'result' via metoden T.orderedTraversal().
        Hvert sorteret element af typen BinNode printes i stigende orden på ny linje.
        
        Search metoden testes på k = 12 og man vil da få følgende iht. testfilerne fra del I:
            T.search: returns True på: positive.txt, same.txt og False på: decreasing.txt, increasing.txt, mixed.txt, negative.txt

        Test eksempel på Windows via PowerShell (med formen: python Treesort.py < inputfile > outputfile):
            >> Get-Content .\Testfiler\increasing.txt | python .\Treesort.py
'''

T = DictBinTree()
n:int = 0

for line in sys.stdin:
    print(line, end='', flush=True) # printer de usorterede input linje for linje 
    T.insert(int(line))
    n += 1

print('T is empty...') if (n<1) else print('Sorting T...')  # printer om T er tom eller kan sorteres

while n > 0:  
    result:list = T.orderedTraversal()    
    print('True: key 12 is in T') if T.search(12) else print('False: key 12 is not in T')  # printer om 12 er en nøgle i T
    print('Sorted Result (ASC):')
    for i in result:
        n -= 1
        print(i)    # printer det sorterede output linje for linje 
