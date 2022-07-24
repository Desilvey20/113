from django.views.generic import (
    ListView, 
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Article
from django.core.exceptions import BadRequest, PermisionDENIED
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, Section, Status



class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "articles/list.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.kwargs.get("status")
        section = self.kwarg.get("section")
        status = Status.objects.get(id=status_id)
        section = Section.objects.get(id=section_id)
        if status == "published":
            context["article_list"] = Article.objects.filter(
               section=section
            ).order_by("created_on").reverse()
             return context
            context["article_list"] = Article.objects.filter(
              status=status
            ).filter(
              section=section
            ).order_by("created_on").reverse()
            return context
        raise PermisionDENIED("You are not authorized to view this page.")


class ArticleDetailView(DetailView):
    template_name = "articles/detail.html"
    model = Article

class ArticleCreateView(CreateView):
    template_name = "articless/new.html"
    model = Article
    fields = [
        "title", "subtitle",
        "body", "status",
        ]

        def form_valid(self, form):
            form.instance.author = self.request.user
            if form.instance.status == "published":
                raise BadRequest(
                    "You are not authorized to publish; Request a review first."
                )
            return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article/edit.html"
    fields = [
        "title", "subtitle",
        "body", "status"
    ]

    def form_valid(self, form):
        if form.instance.status == "published":
            raise BadRequest(
                "You are not authorized to publish; Request a review first."
            )
        return super().form_valid

    
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy("home")
