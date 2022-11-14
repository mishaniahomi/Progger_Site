from django.contrib import admin
from django.urls import path
from .views import TestListView, TestDetaailView
urlpatterns = [
    path('tests/', TestListView.as_view(), name='testlistview'),
    path('test/<int:test_id>', TestDetaailView.as_view(), name='testdetailview'),
]
