from django.urls import path
from .views import WebsiteTemplateView

urlpatterns = [
    path('', WebsiteTemplateView.as_view(), name='index'),
]