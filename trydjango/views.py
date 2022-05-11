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

    # Djando templates
    TITLE = f"""<h1>{article.title} ({article.id})</h1>"""
    CONTENT = f"""<p>{article.content}</p>"""
    HTML_STRING = TITLE + CONTENT

    return HttpResponse(HTML_STRING)