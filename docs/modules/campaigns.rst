.. _campaigns:

********************
Kampanie (campaigns)
********************

Założenia
#########

Moduł zapewnia mechanizm budowania wielu kampanii w ramach indywidualnej instancji aplikacji.
Pozwala to ograniczyć liczbę aplikacij, które będą uruchomione dla różnych kampanii. Dla uruchomienia
dodatkowej instancji aplikacji konieczne jest zagwarantowanie, że

Każda kampania stanowi jedną lub więcej petycji (:ref:`petitions`).

Każda kampania może mieć skonfigurowany indywidualny wystrój, dzięki mechanizmowi szablonów (:ref:`themes`).

Mechanizm kampanii odpowiedzialny jest także za kontrolę dostępu. Umożliwia bowiem określenia użytkowników, którzy bez
uprawnień administracyjnych mają możliwość zarządzania ankietami.

.. _add_campaign:

Dodawanie kampanii
##################

Uruchomienie kampanii wymaga podjęcia następujących kroków:

#. aktualizacja serwera WWW do obsługi nowej domeny
#. aktualizacja dopuszczalnych adresów domenowych - zob. ALLOWED_HOSTS_ poprzez zmienną środowiskową ``DJANGO_ALLOWED_HOSTS``
#. dodawania nowej strony - zob. :any:`django:django.contrib.sites`
#. dodania kampanii w panelu administracyjnym - zob. :any:`petycja_norweskie.campaigns.admin.CampaignAdmin`

.. _ALLOWED_HOSTS: https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts

Architektura
############

Model
-----

.. automodule:: petycja_norweskie.campaigns.models
   :members:


Panel administracyjny
---------------------

.. automodule:: petycja_norweskie.campaigns.admin
   :members:

Widoki
------

.. automodule:: petycja_norweskie.campaigns.views
   :members:

Fabryki
-------

.. automodule:: petycja_norweskie.campaigns.tests.factories
   :members:
