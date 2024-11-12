from django.urls import path
from .views import UsetLisrView

urlpatterns = [
    path('', UsetLisrView.as_view(), name='list_user'),
]