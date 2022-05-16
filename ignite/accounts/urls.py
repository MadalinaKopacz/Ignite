from django.urls import include, path
from . import views

urlpatterns = [  path('create', views.createView),
                 path('detailView/<username>', views.detailView),
                 path('profile', views.profile),
                 path('update/<username>', views.updateView),
                 path('delete/<username>', views.deleteView),
                 path('', include("django.contrib.auth.urls")),
                 path('send_friend', views.findFriendsView, name='send friend request'),
                 path('accept_friend/<requestID>', views.acceptFriendView, name='accept friend request'),
                 path('requests', views.seeFriendRequests)
            ]
            
