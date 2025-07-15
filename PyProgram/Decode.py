import sys
from bitIO import BitReader
import Huffman as hf

""" Dette modul er implementationen af Decode fil-dekompressionen.
    Testes via terminalen som følgende:
        python Decode.py nameOfCompressedFile nameOfDecodedFile
    Den valgte fil dekomprimeres vha. hyppighedtabellen og de genererede kodeord. """

if __name__ == '__main__':
    # læser første argument fra terminalen og åbner input-filen
    infile = open(sys.argv[1], 'rb')
    # læser andet argument fra terminalen og åbner output-filen
    outfile = open(sys.argv[2], 'wb')
    # opretter et objekt BitReader til indlæsning af hyppighedstabellen
    reader = BitReader(infile)
    # variablen til hyppighedstabellen
    alphabet = {}
    
    for i in range(0, 256):
        # indlæser hyppighedstabellen fra input filen som 32-bits integers
        alphabet[i] = reader.readint32bits()

    # bygger huffman-træet udfra hyppighedstabellen
    huffman_tree = hf.huffman(alphabet)
    # udregner størrelsen på output-filen
    outfile_bytes = sum(alphabet.values())
    # gennemløber huffman-træet node for node indtil alle bytes er skrevet til output-filen
    while outfile_bytes > 0:
        # starter ved roden af huffman-træet
        node = huffman_tree
        while True:
            if node.data == -1:
                # hvis noden er en indre kunde (data er -1) 
                # indlæser 1 bit fra input-filen hvor
                bit = reader.readbit()
                if bit == 0:
                    # hvis den indlæste bit er 0, gåes der mod venstre i huffman-træet
                    node = node.left
                else:
                    # hvis den indlæste bit er 1, gåes der mod højre i huffman-træet
                    node = node.right
            else:
                # hvis noden er et blad (data er ikke -1)
                # den gemte data i bladet skrives som 1 byte til output-filen
                outfile.write(bytearray([node.data]))
                # der holdes styr på, hvor mange bytes, der er skrevet til output-filen
                outfile_bytes = outfile_bytes -1
                # da dette er et blad, så startes et nyt gennemløb igen fra roden af huffman-træet
                node = huffman_tree
                break

    reader.close()
    outfile.close()