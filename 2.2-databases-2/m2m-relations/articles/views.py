from django.db.models import Prefetch
from django.shortcuts import render
from .models import Article, ArticleThema


# Create your views here.

def the_article(request):
    ordering = '-published_at'

    context = {
        'object_list': Article.objects.order_by(ordering).prefetch_related(
            Prefetch('themas', queryset=ArticleThema.objects.select_related('thema')))
    }

    return render(request, 'news.html', context)