import sys
from bitIO import BitWriter
import Huffman as hf

""" Dette modul er implementationen af Encode fil-kompressionen.
    Testes via terminalen som følgende:
        python Encode.py nameOfOriginalFile nameOfCompressedFile
    Den valgte fil gemmes med en hyppighedstabel inkl. de genererede kodeord.
    Da de skrevne bits skal være 8, sørger dette modul også for at indsætte eventuelle manglende 0'er. """

if __name__ == '__main__':
    # læser første argument fra terminalen og åbner input-filen
    infile = open(sys.argv[1], 'rb')
    # læser andet argument fra terminalen og åbner output-filen
    outfile = open(sys.argv[2], 'wb')
    # variablen til hyppighedstabellen
    alphabet = {}
    # der oprettes 256 pladser i listen, som alle sættes til 0
    for i in range(0, 256):
        alphabet[i] = 0
    # variabl til at holde styr på om end-of-file er nået
    eof = False
    while not eof:
        # der læses 1-bit fra input-filen
        byte_obj = infile.read(1)
        # der tjekkes for, om det er end-of-file
        eof = len(byte_obj) != 1
        # hvis ikke, da tælles frekvensken for den byte op i hyppighedtabellen
        if not eof:
            if byte_obj[0] in alphabet:
                alphabet[byte_obj[0]] = alphabet[byte_obj[0]] + 1
    # huffman-træet bygges udfra hyppighedstabellen
    huffman_tree = hf.huffman(alphabet)
    # huffman-tabellen bygges udfra huffman-træet
    huffman_table = hf.build_huffman_table(huffman_tree)
    # opretter et objekt BitWriter til skrivning af hyppighedstabellen til output-filen
    writer = BitWriter(outfile)
    # hyppighedstabellen skrives til output-filen som 32-bit integers
    for key,value in alphabet.items():
        writer.writeint32bits(value)
    # der indlæses igen fra input-filens start
    infile.seek(0)
    eof = False
    # der holdes styr på, om der skal indsættes 0-bits i slutningen af output-filen
    bits_written = 0
    while not eof:
        # der indlæses 1 byte fra input-filen
        byte_obj = infile.read(1) 
        eof = len(byte_obj) != 1
        # hvis det ikke er end-of-file, da skrives værdien fra huffman-tabellen som bits til output-filen
        if not eof:
            for c in huffman_table[byte_obj[0]]:
                writer.writebit(int(c))
                bits_written = bits_written + 1
    # hvis der mangler bits i slutningen af output-filen indsættes 0-bits
    while bits_written % 8 != 0:
        writer.writebit(0)
        bits_written = bits_written + 1

    infile.close()
    writer.close()