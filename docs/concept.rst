*******************
Koncepcja aplikacji
*******************

Petycje są formą bezpośredniego uczestnictwa obywateli w procesie sprawowania władzy. Zostały przewidziane w art. 63 Konstytucji RP:

    Każdy ma prawo składać petycje, wnioski i skargi w interesie publicznym, własnym lub innej osoby za jej zgodą do
    organów władzy publicznej oraz do organizacji i instytucji społecznych w związku z wykonywanymi przez nie zadaniami
    zleconymi z zakresu administracji publicznej. Tryb rozpatrywania petycji, wniosków i skarg określa ustawa.

Przedstawiony system został zrealizowany w celu zapewnienia możliwości gromadzenia podpisów pod takimi petycjami w
postaci elektronicznej w sposób efektywny i atrakcyjny dla użytkownika, a tym samym skuteczny.

System został opracowany początkowo na potrzeby kampanii `norweskie.org`_ . Jednak opierał się na wcześniejszych
doświadczeniach Stowarzyszenia Siec Obywatelska - Watchdog Polska między innymi z takimi kampaniami jak:

- `NaszRzecznik.pl`_ - kampania uruchomiona w 2015 roku  celem wsparcia wyboru dr Adama Bodnara na funkcje Rzecznika Praw Obywatelskich - zakończona powodzeniem, w 2016 roku przekształcona w kampanie na rzecz obrony Rzecznika Praw Obywatelskich przed odwołaniem - zakończona powodzeniem,

- :download:`Jawna kampania wyborcza <_static/jawna_kampania.png>` (wyłączona) - kampania uruchomiona w 2015 roku w związku z prezydencką kampanią wyborczą poświęcona presji na opublikowanie jeszcze przed wyborami prezydenckimi aktualizowanej informacji o otrzymanych przez partię w trakcie kampanii wyborczej darowiznach od osób fizycznych, która wywołała szeroką dyskusje o jawności kampanii wyborczej,

- :download:`Poprawka dla Fundacja Akademia Organizacji Obywatelskich <_static/poprawka_faoo.png>` (wyłączona) - kampania przeprowadzona w 2015 roku na przeciwdziałaniu ustawowej poprawce o zakazie finansowania "promocji 1%" ze środków uzyskanych w ramach "mechanizmu 1%" - `zakończona sukcesem`_,

.. _norweskie.org: https://norweskie.org

.. _NaszRzecznik.pl: https://NaszRzecznik.pl

.. _zakończona sukcesem: http://www.faoo.pl/aktualnosci/51-udalo-sie-poprawka-usunieta

Użycie i zasada działania
-------------------------

Korzystanie z aplikacji warto rozpocząć od stworzenia dedykowanego szablonu (zob. :ref:`add_theme`). Następnie dodania
kampanii (zob. :ref:`add_campaign`), utworzenia petycji (zob. :ref:`petitions`). Zadaniem użytkowników strony będzie
utworzenie podpisów (zob. :any:`petycja_norweskie.petitions.models.Signature`).

Aplikacja została skonstruowana wokół kampanii (zob. :ref:`campaigns`), która grupuje jedną lub więcej petycji
(zob. :ref:`petitions`). Poszczególna petycja ma określony formularz, pola w nim, a także wymagane zgody. To w relacji
z petycją znajduą się wszelkie składane podpisy.

