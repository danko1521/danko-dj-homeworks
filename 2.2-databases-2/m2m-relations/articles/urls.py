from django.urls import path

from articles.views import the_article

urlpatterns = [
    path('', the_article, name='articles'),
]
