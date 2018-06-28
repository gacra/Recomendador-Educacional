from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from RecommenderAPI import views

re_questions = r'questions/$'
re_questions_by_topics = (r'questions/'
                          'topics=(?P<topics_text>(([A-Z]+-)*([A-Z]+))|)/$')
re_answers = r'answers/$'
re_materials = r'materials/$'
re_topics_reference = r'topics/$'

urlpatterns = [
    url(re_questions, views.Questions.as_view()),
    url(re_questions_by_topics, views.QuestionsByTopics.as_view()),
    url(re_answers, views.Answers.as_view()),
    url(re_materials, views.Materials.as_view()),
    url(re_topics_reference, views.TopicsReference.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
