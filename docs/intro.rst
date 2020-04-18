.. file "...\docs\intro.rst" (questa riga è un commento!)

Introduzione.
=============

Ecco un esempio di reStructuredText. La sintassi di base è molto semplice: questo è *corsivo*, questo è **neretto**. Un inserto di codice inline 
si produce con due backquote, per esempio ``print('hello world')``. 

I paragrafi sono separati da una riga vuota. 

* Ci sono
* anche le liste, 
* naturalmente.

Nel "dialetto" di Sphinx, Python è naturalmente il linguaggio predefinito. 
Per esempio, per inserire un blocco di codice Python basta usare il 
"doppio due punti"::

    def hello_world():
        return 'hello word'

Questa è una sotto-sezione.
---------------------------

Possiamo usare gli strumenti di ``autodoc`` ovunque. Per esempio, 
ecco come possiamo inserire la documantazione di una classe specifica:

.. autoclass:: mod_uno.FooClass
    :members:
    :noindex:

L'opzione ``noindex`` qui è utile perché questa classe è già documentata 
altrove, e non vogliamo duplicare gli indici. 
