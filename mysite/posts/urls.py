from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'details/<id>/', views.details, name='details'),
    path('new', views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),
    path('drafts', views.post_draft_list, name='post_draft_list'),
    path('<int:id>/publish/', views.post_publish, name='post_publish'),
    path('<int:id>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:id>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:id>/remove/', views.comment_remove, name='comment_remove'),
    path('comment/<int:id>/like/', views.comment_like, name='comment_like'),
]