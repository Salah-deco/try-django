from tkinter import NONE
from django.shortcuts import render
from django.http import HttpResponse

from articles.models import Article

# Create your views here.
def article_search_view(request):
    
    query_dict = request.GET

    try:
        query = query_dict.get('query')
    except:
        query = 0


    article = NONE
    if query is not None:
        article = Article.objects.get(id=query)

    context = {
        "article": article,
    }
    return render(request, 'articles/search.html', context=context)

def article_detail_view(request, id=None):
    # print(id)

    article = None
    if id is not None:
        article = Article.objects.get(id=id)
    else:
        article = Article.objects.get(id=0)
    context = {
        "article": article,
    }
    # return HttpResponse() or use render
    return render(request, "articles/detail.html", context=context)