from django.shortcuts import render
from .models import Contact
from django.urls import reverse_lazy



# Create your views here.
from django.views.generic import ListView
class ContactListView(ListView):
    model = Contact
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'

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

from django.views.generic.edit import UpdateView
class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['Name', 'Email', 'Notes']
    template_name = 'contacts/contact_update.html'
    success_url = '/contact/' # Redirect to the contact list page

    def get_object(self, queryset=None):
        # Retrieve the contact based on the primary key from the form
        pk = self.kwargs.get('pk')
        return Contact.objects.get(pk=pk)
      
from django.views.generic.edit import DeleteView
class ContactDeleteView(DeleteView):
    model = Contact
    success_url = '/contact/'
    template_name = 'contacts/contact_confirm_delete.html'
