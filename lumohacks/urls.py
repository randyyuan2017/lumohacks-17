"""lumohacks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from lumohacks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^pet/$', views.pet_detail, name='pet'),
    url(r'^cbt/$', views.cbt, name='cbt'),
    url(r'^geo/$', views.geo, name='geo'),
    url(r'^map/$', views.map, name='map'),
    url(r'^store/$', views.store, name='store'),
    url(r'^activity/(?P<activity_id>\d+)$', views.activity_detail, name='activity'),
    url(r'^done/(?P<activity_id>\d+)$', views.activity_done, name='done'),
    url(r'^$', views.landing_page, name='landing'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

