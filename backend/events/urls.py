from django.urls import path, include
from .views import *

urlpatterns = [
    path('events/', show_all, name='show_all'),
    path('events/create/', create, name='create'),
    path('events/<uuid:event_id>/edit/', edit, name='edit'),
    path('events/<uuid:event_id>/delete/', delete, name='delete'),
    path('events/<uuid:event_id>/', show_event, name='show_event'),
    path('events/<uuid:event_id>/user/', show_user, name='show_user'),
]