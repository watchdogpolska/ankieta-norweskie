# coding=utf-8
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import message
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, RedirectView, CreateView
from pip.utils import cached_property

from petycja_norweskie.campaigns.models import Campaign
from petycja_norweskie.petitions.forms import SignatureForm
from petycja_norweskie.petitions.models import Signature, Petition

try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse

class ThemedViewMixin:
    @cached_property
    def site(self):
        return get_current_site(self.request)

    @cached_property
    def campaign(self):
        return get_object_or_404(Campaign.objects.select_related('theme'), site=self.site)

    @cached_property
    def template_prefix(self):
        return self.campaign.theme.prefix

    def get_context_data(self, **kwargs):
        kwargs['campaign'] = self.campaign
        return super(ThemedViewMixin, self).get_context_data(**kwargs)

    def get_template_names(self):
        names = super().get_template_names()
        names.append("%s/%s/%s%s.html" % (
            self.model._meta.app_label,
            self.template_prefix,
            self.model._meta.model_name,
            self.template_name_suffix
        ))
        return names


class PetitionMixin:
    @cached_property
    def petition(self) -> Petition:
        qs = Petition.objects.for_user(self.request.user).for_site(self.site)
        return get_object_or_404(qs, slug=self.kwargs['slug'])


class SignatureListView(ThemedViewMixin, PetitionMixin, ListView):
    model = Signature

    def get_paginate_by(self, queryset) -> int:
        return self.petition.paginate_by

    def get_context_data(self, **kwargs):
        kwargs['form'] = SignatureForm(petition=self.petition, campaign=self.campaign)
        kwargs['petition'] = self.petition
        return super(SignatureListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(petition=self.petition)


class PetitionDetailView(ThemedViewMixin, PetitionMixin, DetailView):
    model = Petition

    def get_context_data(self, **kwargs):
        kwargs['form'] = SignatureForm(petition=self.petition, campaign=self.campaign)
        return super(PetitionDetailView, self).get_context_data(**kwargs)

    @cached_property
    def campaign(self):
        return self.object.campaign

    def get_queryset(self):
        return super().get_queryset().for_site(self.site)


class HomePage(ThemedViewMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        petition = get_object_or_404(Petition.objects.for_user(self.request.user).for_site(self.site),
                                     front=True)
        return petition.get_absolute_url()


class SignatureFormView(ThemedViewMixin, PetitionMixin, CreateView):
    model = Signature
    form_class = SignatureForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['petition'] = self.petition
        kwargs['campaign'] = self.campaign
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['petition'] = self.petition
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if not self.petition.is_active:
            messages.warning(self.request, self.petition.disabled_warning)
            return HttpResponseRedirect(self.petition.get_absolute_url())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('petitions:success', kwargs={'slug': self.petition.slug})

    def get_queryset(self):
        return super().get_queryset().filter(petition=self.petition)


class PetitionSuccessView(ThemedViewMixin, DetailView):
    model = Petition
    template_name_suffix = "_success"

    def get_queryset(self):
        return super().get_queryset().for_user(self.request.user).filter(campaign=self.campaign)
