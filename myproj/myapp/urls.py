from django.conf.urls import url
from . import views
from . import cbv, cbv2

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^search/$', views.snippet_search),
    url(r'^cbvsnippets/$', cbv.SnippetList.as_view()),
    url(r'^cbv2snippets/$', cbv2.SnippetList.as_view()),

]