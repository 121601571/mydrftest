from django.conf.urls import url
from . import views
from . import cbv, cbv2
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^books/$', views.book_list),

    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^search/$', views.snippet_search),
    url(r'^cbvsnippets/$', cbv.SnippetList.as_view()),
    url(r'^cbv2snippets/$', cbv2.SnippetList.as_view()),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here

]