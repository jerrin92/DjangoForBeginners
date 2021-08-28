from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article

# Create your views here.
class ArticleListView(ListView, LoginRequiredMixin):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Article
    template_name = 'article_update.html'
    fields = ('title', 'body')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView(DetailView, LoginRequiredMixin):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'

class ArticleCreateView(CreateView, LoginRequiredMixin):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', )
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid()


