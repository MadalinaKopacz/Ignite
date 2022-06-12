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
                 path('login/', views.login_view, name ='login'),
                 path('logout/', views.logout_view, name ='logout'),
                 path('update_location/', views.update_location, name ='update_location'),
            ]
            
