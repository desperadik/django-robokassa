from django.conf.urls import url

from .views import *

app_name = 'robokassa'
urlpatterns = [
    url(
        r'^result/$',
        receive_result,
        name='result'
    ),
    url(
        r'^success/$',
        success,
        name='success'
    ),
    url(
        r'^fail/$',
        fail,
        name='fail'
    ),
]
