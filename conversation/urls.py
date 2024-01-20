from . import views

from django.urls import path, include


app_name = 'conversation'

urlpatterns = [
    path('',views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]