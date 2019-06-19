from django.urls import path, re_path

from . import views

app_name = 'books'
urlpatterns = [
    re_path(r'^$', view=views.BookListView.as_view(), name='index'),
    # re_path(r'^(?P<isbn>[\d\-]+)/$', view=views.BookDetailView.as_view(), name='detail'),
    path("<isbn>/", view=views.BookDetailView.as_view(), name='detail'),
    re_path(r'^create/$', view=views.BookCreateView.as_view(), name='create'),
    re_path(r'^update/(?P<isbn>[\d\-]+)/$', view=views.BookUpdateView.as_view(), name='update'),
    re_path(r'^delete/(?P<isbn>[\d\-]+)/$', view=views.BookDeleteView.as_view(), name='delete'),
]
