from django.urls import path
from . import views

urlpatterns = [path('create/', views.create_activity),
               path('get/', views.get_all_activities),
               path('view/<id>/', views.get_by_id),
               path('view/<id>/delete/', views.delete_activity),
               path('view/<id>/update/', views.update_activity) 
]
