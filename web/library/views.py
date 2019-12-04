from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from .models import Books, Category


class CategoryDetailView(ListView):
    model = Books
    context_object_name = 'objects'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['books'] = Books.object.filter(category=self.kwargs.get('pk'))
    #     context['categories'] = Category.object.filter(name=self.kwargs.get('pk'))
    #     return context

    def get_queryset(self):
        queryset = Books.objects.filter(category=self.kwargs.get('pk')) 
        return queryset


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'



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


class AboutView(TemplateView):
    template_name = "library/about.html"