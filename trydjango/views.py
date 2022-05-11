"""
To render html web pages
"""
from django.http import HttpResponse

HTML_STRING = """<h1>Hello World!</h1>"""

def home(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (we pick to return the response)
    """
    return HttpResponse(HTML_STRING)