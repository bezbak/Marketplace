from django.urls import path
from apps.users.views import register, user_login,account, edit_profile, reset_password, create_password
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', register, name='register'),    
    path('user_login/', user_login, name='user_login'),    
    path('logout/', LogoutView.as_view(next_page='register'), name='logout'),
    path('account/<str:username>', account, name='account'),
    path('edit_profile/<str:username>', edit_profile, name='edit_profile'),
    path('reset_password/', reset_password, name='reset_password'),
    path('create_password/', create_password, name='create_password'),
]
