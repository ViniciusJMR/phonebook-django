from django.shortcuts import render
from django import forms

from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name','last_name','phone',)

appname = 'create'

def create(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
    else:
        contact_form = ContactForm()

    context = {
        'form': contact_form
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
