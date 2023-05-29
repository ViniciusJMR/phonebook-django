from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES)
    else:
        contact_form = ContactForm()

    context = {
        'form': contact_form,
        'form_action': form_action,
    }

    if contact_form.is_valid():
        contact = contact_form.save(commit=False)
        contact.owner = request.user
        contact.save()
        messages.success(request, 'Created Contact!')
        return redirect('contact:update', contact_id=contact.pk)

    return render(
        request,
        'contact/create.html',
        context,
    )


@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    print(contact)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES, instance=contact)
    else:
        contact_form = ContactForm(instance=contact)

    context = {
        'form': contact_form,
        'form_action': form_action,
    }

    if contact_form.is_valid():
        contact = contact_form.save(commit=False)
        # Tratar contato
        contact.save()
        messages.success(request, 'Updated Contact!')
        return redirect('contact:update', contact_id=contact.pk)

    return render(
        request,
        'contact/update.html',
        context,
    )


@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        messages.success(request, 'Deleted Contact!')
        return redirect('contact:index')
    # contact.delete()

    # return redirect('contact:index')
    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )
