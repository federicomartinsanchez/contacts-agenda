from django.conf.urls import url
from . import views

app_name = 'contacts'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^nuevo-contacto/$',views.ContactoCreate.as_view(),name='nuevo-contacto'),
    url(r'^contacto/(?P<pk>[0-9]+)/$',views.ContactoUpdate.as_view(),name='actualizar-contacto'),
    url(r'^contacto/(?P<pk>[0-9]+)/borrar/$',views.ContactoDelete.as_view(),name='borrar-contacto'),

]
