from django import forms
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView, CreateView

from src.apps.panel.models import ClaimTempModel


class ClaimListView(ListView):
    template_name = 'claim-list.html'
    queryset = ClaimTempModel.objects.all()


class ClaimDetailView(DetailView):
    template_name = 'claim-detail.html'
    model = ClaimTempModel


class ClaimCreateView(CreateView):
    success_url = '/panel/list/'
    model = ClaimTempModel
    template_name = 'claim-form.html'
    fields = [
        'title',
        'date_with',
        'date_out',
        'type_chaim',
        'category',
        'priority',
        'organization',
        'master',
        'assignee',
        'info',
        'phone',
        'fio',
        'email',
        'personal_bill',
        'city',
        'district',
        'street',
        'home_number',
        'room_number',
        'intercom',
        'floor',
        'other_info'
        ]
