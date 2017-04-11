# coding=utf-8
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.utils.translation import ugettext as _

from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name="home"),
    url(_(r'^(?P<slug>[\w-]+)/create$'), views.SignatureFormView.as_view(), name="form"),
    url(_(r'^(?P<slug>[\w-]+)/thank$'), views.PetitionSuccessView.as_view(), name="success"),
    url(_(r'^(?P<slug>[\w-]+)$'), views.PetitionDetailView.as_view(), name="petition"),
    url(_(r'^(?P<slug>[\w-]+)/signature$'), views.SignatureListView.as_view(), name="signature"),
    url(_(r'^(?P<slug>[\w-]+)/signature-(?P<page>\d+)$'), views.SignatureListView.as_view(),
        name="signature"),
]
