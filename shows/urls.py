from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),

    path('', views.home, name='home'),

    path('show/<str:pk>/', views.shows, name='show'),
    path('post-show/', views.post_show, name="post-show"),
    path('update-show/<str:pk>/', views.update_show, name="update-show"),
    path('delete-show/<str:pk>/', views.delete_show, name="delete-show"),

    path('profile/<str:pk>/', views.user_profile, name='user-profile'),

]