"""
To render html web pages
"""
from django.http import HttpResponse

from articles.models import Article
from django.template.loader import render_to_string, get_template

def home(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (we pick to return the response)
    """
    # from the database
    article = Article.objects.get(id=2)

    context = {
        "id": article.id,
        "title": article.title,
        "content": article.content
    }

    # Djando templates
    template = get_template("home-view.html")
    template_string = template.render(context=context)
    # HTML_STRING = render_to_string("home-view.html", context=context)


    return HttpResponse(template_string)