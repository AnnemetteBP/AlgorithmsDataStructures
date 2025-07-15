import PQHeap
from Element import Element

"""  Node sørger for at Node / Element objektet får flg. properties left og right. """
class Node(Element):
    def __init__(self,
                 left:Element,
                 right:Element) -> None:
        
        self.left = left
        self.right = right


""" Laver den tomme prioritetskø defineret i PQHeap og indsætter Element objekter. """
def createHeap(C:dict) -> list:
    Q = PQHeap.createEmptyPQ()

    for k, v in C.items():
        PQHeap.insert(Q, Element(v, k))

    return Q


""" Implementation af pseudokode side 434 (HUFFMAN(C)).
    Node objekter er indre knuder og deres data er altid -1.
    Dette er for at kunne skelne mellem indre knuder og blade.
    Blade vil altid betegnes som Elements.
    Deres (Elements) data er så den originale data læst fra input-filen."""
def huffman(C:dict) -> Node:
    Q = createHeap(C)

    while len(Q) > 1:
        x:Element = PQHeap.extractMin(Q)
        y:Element = PQHeap.extractMin(Q)
        z:Node = Node(x, y)
        z.data = -1
        z.key = x.key + y.key
        x.key = str(0)
        y.key = str(1)
        PQHeap.insert(Q, z)

    return PQHeap.extractMin(Q)


""" Itererer huffman-træet og angiver kodeord.
    Er knuden en venstre knude, er karakteren i kodeordet 0.
    Er knuden i stedet en højre knude, da er karakteret i kodeordet 1. """
def iterate_huffman_tree(root:Node, path:str, huffman_table:dict) -> None:
    if root.data == -1:
        iterate_huffman_tree(root.left, str(path + '0'), huffman_table)
        iterate_huffman_tree(root.right, str(path + '1'), huffman_table)
    else:
        huffman_table[root.data] = path


""" Bygger huffman-træet ved rekursivt kald til funktionen iterate_huffman_tree """
def build_huffman_table(root:Node) -> dict:
    huffman_table = {}
    for i in range(0, 256):
        huffman_table[i] = 0
    iterate_huffman_tree(root.left, '0', huffman_table)
    iterate_huffman_tree(root.right, '1', huffman_table)
    
    return huffman_table