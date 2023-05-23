from django.shortcuts import render, redirect
from contact.forms import ContactForm


appname = 'create'

def create(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
    else:
        contact_form = ContactForm()

    if contact_form.is_valid():
        contact = contact_form.save(commit=False)
        # Tratar contato
        contact.save()
        return redirect('contact:create')


    context = {
        'form': contact_form
    }

    return render(
        request,
        'contact/create.html',
        context,
    )
