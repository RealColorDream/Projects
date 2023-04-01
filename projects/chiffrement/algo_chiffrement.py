def decalage(lettre, decalage) -> str:
    """
    >>> decalage('A', 1)
    'B'
    >>> decalage('Z', 1)
    'A'
    >>> decalage("A", 3)
    'D'
    """
    if ord(lettre) + decalage > ord('Z'):
        return chr(ord(lettre) + decalage - 26)
    else:
        return chr(ord(lettre) + decalage)


def cesar(chaine: str, decalage: int) -> str:
    """
    >>> cesar("NSI",3)
    'QVL'
    """
    chaine = chaine.upper()
    text = ""
    for i in range(len(chaine)):
        id = ord(chaine[i])
        text += chr(id+decalage)
    return text


def cesar_bf(texte):
    liste = []
    for i in range(26):
        liste.append(cesar(texte, -i))
    return liste

#  print(cesar_bf("NSI"))


def vigenere(texte: str, code: str, dechiffre: bool = False) -> str:
    """
    >>> vigenere('JADOREECOUTERLARADIO', 'MUSIQUE')
    'VUVWHYIOIMBULPMLSLYI'
    """
    texte = texte.upper()
    code = code.upper()
    text = ""

    if dechiffre:
        for i in range(len(texte)):
            text += decalage(texte[i], ord('A')-ord(code[i % len(code)]))

    else:
        for i in range(len(texte)):
            text += decalage(texte[i], ord(code[i % len(code)])-ord('A'))

    return text


def vigenere_table():
    for i in range(26):
        print(vigenere('ABCDEFGHIJKLMNOPQRSTUVWXYZ', chr(ord('A')+i)))


#  print(vigenere_table())


def substitution_car(car: str, code: str) -> str:
    """
    >>> substitution_car('A', 'MUSIQUE')
    'M'
    >>> substitution_car('B', 'MUSIQUE')
    'U'
    """
    return code[ord(car)-ord('A')]


def substitution(texte: str, code: str) -> str:
    """
    >>> substitution('INFORMATIQUE', 'AZERTYUIOPQSDFGHJKLMWXCVBN')
    'OFYGKDAMOJWT'
    """
    text = ""
    for i in range(len(texte)):
        text += substitution_car(texte[i], code)
    return text


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
