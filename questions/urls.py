from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^$', views.IndexView.as_view(), name='index')
]
