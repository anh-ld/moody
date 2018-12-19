import unidecode


def Standard(n):
    n = n.lower()
    n = n.title()
    n = n.strip()
    for i in range(len(n)):
        n = n.replace('  ', ' ',)
    return n


def Standard1(n):
    n = unidecode.unidecode(n)
    n = n.lower()
    n = n.title()
    n = n.strip()
    for i in range(len(n)):
        n = n.replace('  ', ' ')
        n = n.replace(' ', '+')
        n = n.replace('-', '+')
        n = n.replace('&', '+')
        n = n.replace(',', '+')
        n = n.replace('.', '+')
    return n
