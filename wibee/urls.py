from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from collect.api.views import PlaceViewSet, CategoryViewSet,  UserViewSet
from wibee import settings


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'categories', CategoryViewSet, base_name='categories')
router.register(r'places', PlaceViewSet, base_name='places')
urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'collect.views.home', name='home'),
    url(r'^$', 'collect.views.index', name='index'),
    # url('^api/users/$', UserCreateView.as_view(), name='user-create'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),

    url(r'^register/$', 'collect.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)