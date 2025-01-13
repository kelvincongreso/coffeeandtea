from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class CustomerListView(ListView):
    model = Customer
    template_name = 'app/customer_list.html'
    context_object_name = 'customer'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'app/customer_detail.html'
    context_object_name = 'customer'


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'app/customer_create.html'
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
    success_url = reverse_lazy('home')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'app/customer_update.html'
    fields = ['first_name','last_name', 'email', 'phone_number', 'address']
    success_url = reverse_lazy('customer')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'app/customer_delete.html'
    success_url = reverse_lazy('customer')