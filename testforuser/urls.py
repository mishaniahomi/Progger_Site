from django.urls import path, include
from .views import TestListView, TestDetaailView, AnswerViewSet, OneQuestion, proverka
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('answers', AnswerViewSet, basename='answer')

urlpatterns = [
    path('proverka', proverka, name='proverka'),
    path('tests/', TestListView.as_view(), name='testlistview'),
    path('test/<int:test_id>', TestDetaailView.as_view(), name='testdetailview'),
    path("tags/<int:question>/", OneQuestion.as_view(), name='queststest'),
    path('', include(router.urls)),
]


