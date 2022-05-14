from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from articles.models import Article
from .forms import ArticleForm
# Create your views here.
def article_search_view(request): 
    query_dict = request.GET
    try:
        query = query_dict.get('query')
    except Exception:
        query = 0

    article = Article.objects.get(id=query) if query is not None else None
    context = {
        "article": article,
    }
    return render(request, 'articles/search.html', context=context)

# @login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = { "form": form }
    
    if form.is_valid(): # == cleaned_data
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        article_object = Article.objects.create(title=title, content=content)
        context["objects"] = article_object
        context["created"] = True
    return render(request, 'articles/create.html', context=context)

# def article_create_view(request):
#     # if not request.user.is_authenticated:
#     #     return redirect('/login')
#     form = ArticleForm()
#     # print(dir(form))
#     context = {
#         "form": form,
#     }

#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         context["form"] = form
        
#         if form.is_valid(): # == cleaned_data
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             article_object = Article.objects.create(title=title, content=content)
#             context["objects"] = article_object
#             context["created"] = True
#     return render(request, 'articles/create.html', context=context)
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