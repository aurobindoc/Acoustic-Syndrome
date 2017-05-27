from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page /music
    url(r'^$', views.index, name='index'),

    # Detailed Artist /music/<artist_id>
    url(r'^(?P<artist_id>[0-9]+)$', views.detail, name='detail'),
]
