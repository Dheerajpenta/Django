from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from color_picker import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url('', views.srcList.as_view()),
]
