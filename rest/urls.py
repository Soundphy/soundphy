from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest import views


urlpatterns = [
    url(r'^sounds/$', views.SoundList.as_view()),
    url(r'^sounds/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
