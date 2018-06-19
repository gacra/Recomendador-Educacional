from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from RecommenderApp import views

re_questions_all = r'^questions/$'
re_questions = r'^questions/topics=(?P<topics_text>(([A-Z]+-)*([A-Z]+))|)/$'
re_answers = r'^answers/$'
re_materials = r'^materials/$'

urlpatterns = [
    url(re_questions_all, views.QuestionsAll.as_view()),
    url(re_questions, views.Questions.as_view()),
    url(re_answers, views.Answers.as_view()),
    url(re_materials, views.Materials.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
