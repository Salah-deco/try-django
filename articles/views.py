from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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

@login_required
def article_create_view(request):
    # if not request.user.is_authenticated:
    #     return redirect('/login')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        context["created"] = True
    context = {}
    return render(request, 'articles/create.html', context=context)

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