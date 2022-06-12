from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [  path('create/', views.createView, name='create'),
                 path('detailView/<username>/', views.detailView),
                 path('profile/', views.profile),
                 path('update/<username>/', views.updateView),
                 path('delete/<username>/', views.deleteView),
                 #  path('', include("django.contrib.auth.urls")),
                 path('send_friend/', views.findFriendsView, name='send friend request'),
                 path('accept_friend/<requestID>/', views.acceptFriendView, name='accept friend request'),
                 path('requests/', views.seeFriendRequests),
                 path('login/', auth_views.LoginView.as_view(template_name='../templates/accounts/login.html'), name ='login'),
                 path('logout/', views.logout_view, name ='logout'),
            ]
            
