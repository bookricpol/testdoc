"""In questo modulo dimostriamo alcune altre cose.

Per esempio, così è possibile linkare a :py:class:`mod_uno.FooClass`.
"""

FOO = 42 #: ecco una costante: Sphinx legge il "#:"

BAR = 'hello'
"""Questa costante è documentata con una docstring."""

# questa è una funzione non documentata
def bar_funct(a, b, c):  
    pass

class BarClass:
    """Questa classe contiene metodi 'privati' e 'speciali'."""

    baz = 'baz' #: un attributo di classe

    def _private_meth(self):
        """Questo è un metodo privato."""
        pass

    def __eq__(self, other):
        """Questo è un metodo speciale."""
        pass

    def __special_meth__(self):
        """Un metodo speciale nuovo.

        Si noti che non è consigliato inventare nuovi metodi speciali.
        """
