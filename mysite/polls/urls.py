from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'polls'

try:
    urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        path('moods', views.MoodsView.as_view(), name='moods'),
        url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    ]
    # MoodView
except:
    print("ERROR")