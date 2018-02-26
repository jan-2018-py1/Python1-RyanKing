from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^books$', views.books),
    url(r'^books/(?P<num>\d+)$', views.display_book),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^add_book$', views.add_book),
    url(r'^add_review$', views.add_review),
    url(r'^users/(?P<num>\d+)$', views.show_user),
    url(r'^delete/(?P<num>\d+)$', views.delete)
]
