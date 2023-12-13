from django.shortcuts import render
from .models import Contact
from django.urls import reverse_lazy



# Contact_management_view
from django.views.generic import ListView
class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'
    
#Create_contact_view
from django.views.generic import DetailView
class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'

from django.views.generic.edit import CreateView
class ContactCreateView(CreateView):
    model = Contact
    fields = ['Name', 'Email', 'Notes']
    success_url = '/contact/'
    template_name = 'contacts/contact_form.html'