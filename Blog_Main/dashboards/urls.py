from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),

    path('categories/', views.categories, name = 'categories'),
    path('categories/add/', views.add_categories, name = 'add_categories'),
    path('categories/edit/<int:cat_id>', views.edit_categories, name = 'edit_categories'),
    path('categories/delete/<int:cat_id>', views.delete_categories, name = 'delete_categories'),

    path('posts/', views.posts, name = 'posts'),
    path('posts/add/', views.add_post, name = 'add_post'),
    path('posts/edit/<int:post_id>', views.edit_post, name = 'edit_post'),
    path('posts/delete/<int:post_id>', views.delete_post, name = 'delete_post'),

    path('users/', views.users, name = 'users'),
    path('users/add', views.add_user, name = 'add_user'),
    path('users/edit/<int:user_id>', views.edit_user, name = 'edit_user'),
    path('users/delete/<int:user_id>', views.delete_user, name = 'delete_user'),

    path('comments/', views.comments, name = 'comments'),
    path('comments/delete/<int:com_id>', views.delete_comment, name = 'delete_comment'),
]
