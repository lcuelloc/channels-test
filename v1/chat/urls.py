from django.conf.urls import url

from v1.chat import views

urlpatterns = [
    url(r'chat/', views.index, name='index'),
]
