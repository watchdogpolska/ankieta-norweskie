Testy
=====

Testy automatyczne zostały oparte o wbudowane w Django mechanizmy. Dostał wykorzystany także domyślny "test runner".
Automatyzacje testów różnych konfiguracji np. wersje zależności zapewnia ``tox``.

Aby wypisać dostępne środowiska należy wykonać::

    tox -l

Wówczas możliwy jest wybór środowiska testów i wykonanie::

    tox -e dj111-coveralls

Zostały wdrożone ciągłe testy integracyjne z wykorzystaniem TravisCI.
