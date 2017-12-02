"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse

from blog import model_view_sets
from blog.feeds import AllPostsRssFeed
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', model_view_sets.UserViewSet)
router.register(r'groups', model_view_sets.GroupViewSet)
router.register(r'category', model_view_sets.CategoryViewSet)
router.register(r'posts', model_view_sets.PostViewSet)
router.register(r'tags', model_view_sets.TagViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    url(r'^robots\.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
    url(r'^search/', include('haystack.urls')),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]
