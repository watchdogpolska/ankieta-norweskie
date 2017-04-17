.. _menu:

***********
Menu (menu)
***********

Założenia
#########

Moduł zapewnia mechanizm menu nawigacyjnego dla poszczególnych stron internetowych. Odnośniki mogą być:

* odnośnikami wewnętrznymi, a wówczas weryfikowana jest zgodność adresów z aplikacją,
  choć to nie znaczy, że pod podanym adresem zawarta jest treść
* odnośnikami zewnętrzne `https://`` lub ``http:``,
* odnośniki e-mailowe ``mailto:``.

Architektura
############

Model
-----

.. automodule:: petycja_norweskie.menu.models
   :members:


Panel administracyjny
---------------------

.. automodule:: petycja_norweskie.menu.admin
   :members:

Procesorzy kontekstu
--------------------

.. automodule:: petycja_norweskie.menu.context_processors
   :members:

Widoki
------

.. automodule:: petycja_norweskie.menu.views
   :members:
