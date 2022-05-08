from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    phone_objects = Phone.objects.all()
    phones = [{'name': phone.name, 'image': phone.image, 'price': phone.price, 'release_date': phone.release_date, 'lte_exists': phone.lte_exists, 'slug': phone.slug} for phone in phone_objects]

    if sort == 'name':
        phones = sorted(phones, key=lambda k: k['name'], reverse=False)
    elif sort == 'min_price':
        phones = sorted(phones, key=lambda k: k['price'], reverse=False)
    elif sort == 'max_price':
        phones = sorted(phones, key=lambda k: k['price'], reverse=True)

    template = 'catalog.html'
    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    phone_objects = Phone.objects.filter(slug=slug)
    phone = dict()
    for item in phone_objects:
        phone = {
            'name': item.name,
            'image': item.image,
            'price': item.price,
            'release_date': item.release_date,
            'lte_exists': item.lte_exists,
            'slug': item.slug
        }
    print(phone)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)
