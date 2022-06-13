from django.test import TestCase
from django.urls import reverse

from mood_quizzes.forms import QuestionCreateForm
from mood_quizzes.models import Question


# Create your tests here.
class QuizTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for q_id in range(10):
            Question.objects.create(title=f'{q_id}',text=f'Text {q_id}',qtype = q_id%3+1)


    def test_qtype_options(self):
        form = QuestionCreateForm()
        choices = form.fields['qtype'].choices
        self.assertEqual(choices, [('', '---------'), (1, 'Social'), (2, 'Physical'), (3, 'Money')])
        
    def test_text_max_length(self):
        textTest = 'a'*301
        form = QuestionCreateForm(data={'qtype': 1, 'text': textTest})
        self.assertFalse(form.is_valid())
        textTest = 'a'*300
        form1 = QuestionCreateForm(data={'qtype': 1, 'text': textTest})
        self.assertTrue(form1.is_valid())
        textTest = 'a'*150
        form2 = QuestionCreateForm(data={'qtype': 1, 'text': textTest})
        self.assertTrue(form2.is_valid())


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/mood_quizzes/createQuestion/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('mood_quizzes:quiz'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quizzes/quiz.html')
