"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'api', tasks_list)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^', include(router.urls)),
    url(r'^tasks/$', views.TasksList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)