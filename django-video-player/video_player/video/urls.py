from django.urls import path
from .views import history_addview, history_list, bookmark_addview, bookmark_list

urlpatterns = [
    path('', history_addview, name='history-add'),
    path('history/list/', history_list, name='history-list'),
    path('bookmark/list/', bookmark_list, name='bookmark-list'),
    path('bookmark/add/', bookmark_addview, name='bookmark-add'),
]