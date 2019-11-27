from django.urls import path
from .views import BookDetailView, BookListView

urlpatterns = [
    path('<slug>', BookDetailView.as_view(template_name='library/book.html'), name="book-detail"),
    path('', BookListView.as_view(template_name='library/index.html'), name="home"),
]