from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from .models import Books


class BookListView(ListView):
    model = Books
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Books
    context_object_name = 'book'


class HomePageView(ListView):
    template_name = 'library/home.html'
    queryset = Books.objects.all()


class SearchResultsView(ListView):
    model = Books
    template_name = 'library/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Books.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return object_list


