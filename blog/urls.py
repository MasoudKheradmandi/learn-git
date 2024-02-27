from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.ApiIndexView.as_view(), name='hello-world'),
    path('tag/', views.ApiTag.as_view(),name='tag')
]