from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area') # name=search_area
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ""
    return render(request, 'contact/index.html', {'contacts':contacts, 'search_input': search_input})

def add_contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number = request.POST['phone-number'],
            address = request.POST['address'],
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'contact/new.html')

def contact_profile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact/contact-profile.html', {'contact':contact})

def edit_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/profile/' + str(contact.id))
    return render(request, 'contact/edit.html', {'contact':contact})


def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'contact/delete.html', {'contact':contact})

 