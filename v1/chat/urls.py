from django.conf.urls import url

from v1.chat import views

urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'(?P<room_name>[^/]+)/$', views.room, name='room'),
]
