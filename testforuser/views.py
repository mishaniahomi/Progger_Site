from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Test
from .serializers import AnswerSerializer, QuestionSerializer
from rest_framework import viewsets, filters, permissions, generics
from .models import Answer, Question


class AnswerViewSet(viewsets.ModelViewSet):
    search_fields = ["id", "title", "question_id"]
    filter_backends = (filters.SearchFilter,)
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [permissions.AllowAny]


class OneQuestion(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        question = self.kwargs['question']

        return Question.objects.filter(test_id=question)





class TestListView(ListView):
    model = Test
    context_object_name = 'Tests'
    paginate_by = 9

    def get_queryset(self):
        filter_val = self.request.GET.get('filter')
        if filter_val is not None:
            if filter_val.isdigit():
                return Test.objects.filter(category=filter_val)
        return Test.objects.all()


class TestDetaailView(DetailView):
    model = Test
    pk_url_kwarg = 'test_id'




