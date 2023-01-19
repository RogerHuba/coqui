from django.urls import path
from .views import CoquiHomeView

urlpatterns = [
    path('', CoquiHomeView.as_view(), name='index'),
]