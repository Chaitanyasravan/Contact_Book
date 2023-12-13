from django.shortcuts import render
from .models import Contact
from django.urls import reverse_lazy



# Contact_management_view
from django.views.generic import ListView
class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'
    
