from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [  path('create/', views.createView, name='create'),
                 # path('detailView/<username>/', views.detailView),
                 path('profile/', views.profile, name="profile"),
                 path('update/', views.updateView, name="update"),
                 path('changepassword/', views.changePasswordView, name="chpass"),
                 path('delete/<username>/', views.deleteView),
                 #  path('', include("django.contrib.auth.urls")),
                 path('send_friend/', views.findFriendsView, name='search'),
                 path('accept_friend/<requestID>/', views.acceptFriendView, name='accept friend request'),
                 path('requests/', views.seeFriendRequests, name="requests"),
                 path('login/', views.login_view, name ='login'),
                 path('logout/', views.logout_view, name ='logout'),
            ]
            
