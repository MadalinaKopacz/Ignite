from django.urls import path
from . import views

urlpatterns = [ path('createQuestion', views.createView),
                path('readQuestions/', views.listView),
                path('readQuestions/<type>/', views.questionsByType),
                path('readQuestion/<id>/', views.questionById),
                path('deleteQuestion/<id>/', views.deleteQuestionById),
                path('deleteQuestions/<type>/', views.deleteQuestionsByType),
                path('deleteAllQuestions/', views.deleteAllQuestions),
                path('updateQuestionType/<id>', views.updateType),
                path('updateQuestionText/<id>', views.updateText),
                path('updateQuestion/<id>', views.updateQuestion)
]
