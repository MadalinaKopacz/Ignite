from django.urls import path
from . import views

urlpatterns = [path('create/', views.create_activity),
               path('get/', views.get_all_activities),
               path('view/<id>/', views.get_by_id),
               path('<id>/delete/', views.delete_activity),
               path('<id>/update/', views.update_activity),
               path('<socialScore>/<physicalScore>/<moneyScore>/<weather>/<counter>/', views.chooseActivities, name='choose_activity'),
               path('<lon>/<lat>/', views.start_activity, name='explorer'), 
               path('map/', views.explore, name='map') 
]
