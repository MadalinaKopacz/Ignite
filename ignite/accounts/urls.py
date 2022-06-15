from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [  path('create/', views.create_view, name='create'),
                 path('profile/', views.profile, name="profile"),
                 path('update/', views.update_view, name="update"),
                 path('changepassword/', views.change_password_view, name="chpass"),
                 path('delete/<username>/', views.delete_view),
                 path('send_friend/', views.find_friends_view, name='search'),
                 path('accept_friend/<requestID>/', views.accept_friend_view, name='accept_friend_request'),
                 path('requests/', views.see_friend_requests_view, name="requests"),
                 path('login/', views.login_view, name ='login'),
                 path('logout/', views.logout_view, name ='logout'),
            ]
            
