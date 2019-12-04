from django.urls import path
from .views import BookDetailView
urlpatterns = [
    path('<slug>', BookDetailView.as_view(template_name='library/book.html'), name="book-detail"),
]   