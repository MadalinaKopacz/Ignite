from django.urls import path
from . import views

urlpatterns = [ path('createQuestion/', views.create_view),
                path('readQuestions/', views.list_view),
                path('readQuestions/<qtype>/', views.questions_by_type),
                path('readQuestion/<id>/', views.question_by_id),
                path('deleteQuestion/<id>/', views.delete_question_by_id),
                path('deleteQuestions/<qtype>/', views.delete_questions_by_type),
                path('deleteAllQuestions/', views.delete_all_questions),
                path('updateQuestionType/<id>/', views.update_type),
                path('updateQuestionText/<id>/', views.update_text),
                path('updateQuestion/<id>/', views.update_question),
                path('quiz/', views.get_quiz, name='quiz')
]
