# coding=utf-8
from django.shortcuts import get_object_or_404
# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, RedirectView, CreateView
from pip.utils import cached_property

from petycja_norweskie.petitions.forms import SignatureForm
from petycja_norweskie.petitions.models import Signature, Petition


class PetitionMixin:
    @cached_property
    def petition(self) -> Petition:
        qs = Petition.objects.for_user(self.request.user)
        return get_object_or_404(qs, slug=self.kwargs['slug'])


class SignatureListView(PetitionMixin, ListView):
    model = Signature

    def get_paginate_by(self, queryset) -> int:
        return self.petition.paginate_by

    def get_context_data(self, **kwargs):
        kwargs['form'] = SignatureForm(petition=self.petition)
        kwargs['petition'] = self.petition
        return super(SignatureListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(petition=self.petition)


class PetitionDetailView(DetailView, PetitionMixin):
    model = Petition

    def get_context_data(self, **kwargs):
        kwargs['form'] = SignatureForm(petition=self.petition)
        return super(PetitionDetailView, self).get_context_data(**kwargs)


class HomePage(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return get_object_or_404(Petition.objects.for_user(self.request.user), front=True).get_absolute_url()


class SignatureFormView(PetitionMixin, CreateView):
    model = Signature
    form_class = SignatureForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['petition'] = self.petition
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['petition'] = self.petition
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('petitions:success', kwargs={'slug': self.petition.slug})


class PetitionSuccessView(DetailView):
    model = Petition
    template_name_suffix = "_success"

    def get_queryset(self):
        return super().get_queryset().for_user(self.request.user)
