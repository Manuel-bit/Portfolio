from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.Index, name='Home'),
    url(r'projects-bccis/$',views.Bccis, name='Berea'),

]