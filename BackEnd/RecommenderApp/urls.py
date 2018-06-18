from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from RecommenderApp import views

urlpatterns = [
    url(r'^questions/$', views.QuestionsAll.as_view()),
    url(r'^questions/topics=(?P<topics_text>(([A-Z]+-)*([A-Z]+))|)/$', views.Questions.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)