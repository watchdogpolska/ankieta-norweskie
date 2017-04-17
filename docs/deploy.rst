.. _deploy:

Wdrożenie
=========

Wdrożenie aplikacji wymaga:

* dostępności Python>3.3 i menadżera pakietów ``pip``,
* skonfigurowania serwera baz danych MariaDB,
* wywołania serwera aplikacyjnego gunicorn,
* skonfigurowania serwera Nginx jako reverse-proxy w Gunicorn.

Ponadto konieczne jest ustawienie następujących zmiennych środowiskowych:

* ``DJANGO_SECRET_KEY`` - losowa i poufność wartość zgodnie z dokumentacją Django dla SECRET_KEY_,
* ``DJANGO_SETTINGS_MODULE`` o wartości ``config.settings.production`` dla określenie pliku konfiguracyjnego
  wykorystanego po załadowaniu aplikacji,
* ``DJANGO_SENTRY_DSN`` - adres `Sentry DSN`_ służacy do wskazania narzędzia monitoringu wyjątków,
* ``DJANGO_ADMIN_URL``` o wartości np. "admin/" dla określenia ścieżki panelu administracyjnego,
* ``CACHE_URL`` o wartości zgodnej z django-environ_ dla ustawienia mechanizmu cache.

.. _SECRET_KEY: https://docs.djangoproject.com/en/1.11/ref/settings/#secret-key
.. _`Sentry DSN`: https://docs.sentry.io/quickstart/#about-the-dsn
.. _django-environ: https://github.com/joke2k/django-environ


W środowisku Stowarzyszenie wdrożenie odbywa się z wykorzystaniem roli Ansible ``watchdogpolska.django``.
