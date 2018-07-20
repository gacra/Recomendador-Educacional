FROM python:3
ENV PYTHONUNBUFFERED 1

ADD ./RecommenderServer/RecommenderAPI /RecommenderServer/RecommenderAPI
ADD ./RecommenderServer/RecommenderProj /RecommenderServer/RecommenderProj
ADD ./RecommenderServer/manage.py /RecommenderServer/manage.py
ADD ./RecommenderServer/requirements.txt /RecommenderServer/
RUN mkdir /RecommenderServer/RecommenderAPI/migrations

ADD ./Utils/rec_edu_utils /Utils/rec_edu_utils
ADD ./Utils/setup.py /Utils/

WORKDIR /Utils
RUN pip install .
WORKDIR /RecommenderServer
RUN pip install -r requirements.txt