from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>\d+)/$', views.snipet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
