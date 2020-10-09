from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Image, Contact
from django.contrib import messages
# Create your views here.


def index(request):
    pic_list = Image.objects.all()
    paginator = Paginator(pic_list, 6)
    page = request.GET.get('page')
    try:
        pics = paginator.page(page)
    except PageNotAnInteger:
        pics = paginator.page(1)
    except EmptyPage:
        pics = paginator.page(paginator.num_pages)
    context = {
        'page': page,
        'pics': pics
    }
    return render(request, 'MyImageAdda/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        # Saving to the database
        if name == '' or email == '' or content == '':
            messages.error(request, 'Please fill the form correctly.')
        else:
            contact = Contact(name=name, email=email, content=content)
            contact.save()
            messages.success(
                request, 'Your message has been sent successfully!')
    return render(request, 'MyImageAdda/contact.html')
