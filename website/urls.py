from django.urls import path
from .views import WebsiteTemplateView, index

urlpatterns = [
    # path('', WebsiteTemplateView.as_view(), name='index'),
    path('', index)
]