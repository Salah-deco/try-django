from tkinter import NONE
from django.shortcuts import render
from django.http import HttpResponse

from articles.models import Article

# Create your views here.
def article_detail_view(request, id=None):
    print(id)

    article = None
    if id is not None:
        article = Article.objects.get(id=id)
    else:
        article = Article.objects.get(id=0)
    print(article)
    context = {
        "article": article,
    }
    # return HttpResponse() or use render
    return render(request, "articles/detail.html", context=context)