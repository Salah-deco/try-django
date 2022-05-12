"""
To render html web pages
"""
from django.http import HttpResponse

from articles.models import Article
from django.template.loader import render_to_string

def home(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (we pick to return the response)
    """
    # from the database
    article = Article.objects.get(id=2)
    articles = Article.objects.all() # type: QuerySet
    

    context = {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "articles": articles
    }

    # Djando templates
    # render_to_string, get_template and select_template 
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)