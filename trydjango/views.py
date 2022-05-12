"""
To render html web pages
"""
from django.http import HttpResponse

from articles.models import Article


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
    HTML_STRING = """
    <h1>{title} ({id})</h1>
    <p>{content}</p>
    """.format(**context)


    return HttpResponse(HTML_STRING)