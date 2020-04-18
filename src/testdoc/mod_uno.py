"""Questa è la docstring del modulo. 

Qui di solito si introducono le funzionalità del modulo e talvolta 
si fanno degli esempi. In reStructuredText è facile inserire un 
blocco di codice Python in questo modo::

    >>> print('hello world')
    'hello world'
"""

def foo_funct():
    """Questa funzione ha una dostring mono-linea."""
    pass

class FooClass:
    """Questa è la docstring della *classe* FooClass."""

    def __init__(self, a, b=None):
        "Questa invece è la docstring di ``__init__``."
        pass

    def foo_meth(self, a, b, c, d):
        """Qui mostriamo come documentare i parametri. 

        :param str a: Spiegazione del parametro "a" (una stringa)
        :param int b: Spiegazione del parametro "b" (un intero)
        :param c: Per "c" indichiamo il tipo separatamente
        :type c: int or None
        :param d: Il parametro "d" è una lista di interi
        :type d: list[int]
        :return: Spiegazione di che cosa viene restituito
        :rtype: tuple(str)
        :raises ValueError: Quando emette una particolare eccezione
        :raises TypeError: Un'altra eccezione possibile
        """
