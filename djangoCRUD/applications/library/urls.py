from django.urls import path

from applications.library import views

urlpatterns = [
    path('library/list', views.list_all_book, name='list'),
    path('library/book/create', views.create_book, name='create'),
    path('library/book/<book_id>/get', views.get_book, name='get'),
    path('library/book/edit', views.edit_book, name='edit'),
    path('library/book/<book_id>/delete', views.delete_book, name='delete')

]
