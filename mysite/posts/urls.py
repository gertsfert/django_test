from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'details/<id>/', views.details, name='details'),
    path('new', views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),
    path('drafts', views.post_draft_list, name='post_draft_list'),
]