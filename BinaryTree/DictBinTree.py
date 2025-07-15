'''
    Gruppe:

    PART II: OPGAVE 1:

        Implementation af bogens pseudo-kode for ubalancerede søgetræer til et Python-program (Cormen et al. 4 udgave kapitel 12).
        Programmet implementerer datastrukturen binært søgetræ med tal som nøgler.
        
        Pseudo-kode side 314 (kode linje 88-99):
            INORDER-TREE-WALK(x) -> public orderedTraversal og private __orderedTraversal:
                Public list orderedTraversal retunerer en liste med nøglerne sorteret i stigende orden.
                Private void __orderedTraversal er selve implementationen af sorteringen og kaldes af orderedTraversal.

        Pseudo-kode side 316 (kode linje 46-57):
            TREE-SEARCH(x,k) -> public search og private __search:
                Søger fra roden og ned for at sammenligne heltallet k med eksisterende nøgler i træet.
                Public bool search kalder private rekursive __search. Hvis en BinNode er None (NIL) findes nøglen k ikke i træet.
                __search udfører den egentlige search procedure og retunerer et objekt af typen BinNode. Denne kan være None (NIL), eller have værdien k.

        Pseudo-kode side 321 (kode linje 62-83):
            TREE-INSERT(T,z) -> insert:
                Public void insert indsætter ny knude af typen BinNode med værdi k i træet (T).
                Ligeldes TREE-SEARCH(x,k), evaluerer proceduren fra roden og ned i træets grene.
'''

class BinNode:
    ''' BinNode: en node / knude objekt i træet, der instansieres med 4 properties: parent, left-child, right-child og k (key). '''
    def __init__(self, k:int) -> None:
        self.parent:BinNode = None
        self.left:BinNode = None
        self.right:BinNode = None
        self.k:int = k


class DictBinTree:
    ''' DictBinTree: selve søgetræet (T), der implementerer 0 eller flere objekter af typen BinNode og instansieres med propertien root. '''
    def __init__(self) -> None:
        self.root:BinNode = None


    ''' search og __search: pseudo-kode side 316 '''

    def search(self, k:int) -> bool:
        ''' T.search(k) returnerer en Boolean, der angiver om nøglen k er i træet T. '''
        return True if self.__search(self.root, k) is not None else False
    
    def __search(self, x:BinNode, k:int) -> BinNode:
        if x is None or k == x.k:
            return x
        
        if k < x.k:
            return self.__search(x.left, k)
        else:
            return self.__search(x.right, k)
        
    
    ''' insert: pseudo-kode side 321 '''

    def insert(self, k:int) -> None:
        ''' T.insert(k) indsætter nøglen k i træet T. '''
        z = BinNode(k)
        x:BinNode = self.root
        y:BinNode = None

        while x is not None:
            y = x

            if z.k < x.k:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y is None:
            self.root = z
        elif z.k < y.k:
            y.left = z
        else:
            y.right = z


    ''' orderedTraversal og __orderedTraversal: pseudo-kode side 314 '''
     
    def orderedTraversal(self) -> list:
        ''' T.orderedTraversal() returnerer en liste med nøglerne i træet T i sorteret orden fremfor at printe. '''
        result:list = []

        self.__orderedTraversal(self.root, result)
        return result
    
    def __orderedTraversal(self, x:BinNode, result:list) -> None:
        if x is not None:
            self.__orderedTraversal(x.left, result)
            result.append(x.k)
            self.__orderedTraversal(x.right, result)
