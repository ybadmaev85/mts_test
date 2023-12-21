from django.urls import path

from new_app.apps import NewAppConfig
from new_app.views import index, index2, index3, my_view

app_name = NewAppConfig.name


urlpatterns = [
    path('', index, name='index'),
    path('index2/', index2, name='index2'),
    path('index3/', index3, name='index3'),
]
