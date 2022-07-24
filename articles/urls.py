from django.urls import path
from articles import views

urlpatterns = [
    path('<section>/<section>', views.ArticleListView.as_view(),name="article_list"),
    path('<ink:pk>/', views.ArticleDetailView.as_view(),name="article_detail"),
    path('<ink:pk>/edit/', views.ArticleUpdateView.as_view(),name="article_edit"),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(),name="article_delete"),
]