from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contact.models import Contact
from django.http import Http404
from django.db.models import Q

def index(request):
    #contacts = Contact.objects.all().order_by('-id')
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts ,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
        'site_title':'Contatos - '
    }
    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):

    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('contact:index')
    contacts = Contact.objects.filter(show=True).order_by('-id').filter(
        Q(id__icontains=search_value) | 
        Q(first_name__icontains=search_value) | 
        Q(last_name__icontains=search_value))
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):

    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact.objects, pk=contact_id, show=True)  

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '  
    context = {
        'contact':single_contact,
        'site_title':site_title,
    }
    return render(
        request,
        'contact/view.html',
        context
    )
