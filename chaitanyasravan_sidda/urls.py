"""
URL configuration for chaitanyasravan_sidda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from contacts import views
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url = 'contact/', permanent=False)),
    path('contact/', views.ContactListView.as_view(), name='contact_list'),
    path('contact/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('contact/create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contact/<int:pk>/update/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('contact/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
]
