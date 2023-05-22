from django.shortcuts import render
from contact.forms import ContactForm


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
