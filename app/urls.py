from django.urls import path
from .views import (HomePageView, AboutPageView, MenuPageView, ReviewPageView, BookPageView, BookATablePageView, CustomerListView, CustomerDetailView,
                    CustomerCreateView, CustomerUpdateView, CustomerDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('menu/', MenuPageView.as_view(), name='menu'),
    path('review/', ReviewPageView.as_view(), name='review'),
    path('book/', BookPageView.as_view(), name='book'),
    path('book_a_table/', BookATablePageView.as_view(), name='book_a_table'),
    path('customer/', CustomerListView.as_view(), name='customer'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

]