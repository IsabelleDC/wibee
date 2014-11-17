from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from collect.api.views import PlaceViewSet, CategoryViewSet,  UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'categories', CategoryViewSet, base_name='categories')
router.register(r'places', PlaceViewSet, base_name='places')
urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'collect.views.home', name='home'),
    url(r'^index', 'collect.views.index', name='index'),
    # url('^api/users/$', UserCreateView.as_view(), name='user-create'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

)
