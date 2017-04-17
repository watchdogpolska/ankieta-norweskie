.. _petitions:

*******************
Petycje (petitions)
*******************

Założenia
#########

Komponent zapewnia mechanizm petycji, a także gromadzenia pod nimi podpisów, co stanowi podstawowy cel
funkcjonowania projektu. Każda petycja ma określoną kampanie (zob. :ref:`menu` ).

Mechanizm petycji jest szeroko konfigurowalny zapewniając możliwość ukrycia każdego z pól formularzy, co umożliwia
uwzględnienie specyfiki kampanii.

Ponadto jest przewidziana funkcjonalność pól zgód. W celu ich skorzystania należy pierw zdefiniować definicję zgody
dla danej petycji. Można przy tym określić czy zgoda będzie wymagana, czy opcjonalna, a także wzajemną kolejność zgód w
formularzu. Zapewnia to szerokie możliwości uzyskania zgód zgodnie z różnorodnymi potrzebami i wymogami prawa.

Zgromadzone podpisy możliwe są do wyeksportowania w szeregu formatach. Eksport obejmuje także informacje o udzielonych
zgodach.

Architektura
############

Model
-----

.. automodule:: petycja_norweskie.petitions.models
   :members:

Formularze
----------

.. automodule:: petycja_norweskie.petitions.forms
   :members:

Panel administracyjny
---------------------

.. automodule:: petycja_norweskie.petitions.admin
   :members:

Widoki
------

.. automodule:: petycja_norweskie.petitions.views
   :members:

Fabryki
-------

.. automodule:: petycja_norweskie.petitions.tests.factories
   :members:
