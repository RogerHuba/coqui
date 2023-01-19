from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from datetime import datetime
from django.http import HttpResponse


class WebsiteTemplateView(TemplateView):
    # template_name = "index.html"
    pass


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from the Coqui</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)