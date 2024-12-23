from django.urls import path
from .views import UsetLisrView,BookDetailView

urlpatterns = [
    path('', UsetLisrView.as_view(), name='list_user'),
    path('<int:book_id>/',BookDetailView.as_view(),name='book-detail')
]