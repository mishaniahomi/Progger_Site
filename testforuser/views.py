from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Test, Answer, Question, Kit
from .serializers import AnswerSerializer, QuestionSerializer
from rest_framework import viewsets, filters, permissions, generics
from django.http import JsonResponse
import json

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


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def proverka(request):
    if request.method == 'POST':
        data_bytes = request.body
        data_dict = json.loads(data_bytes.decode('utf-8'))
        question_count = Question.objects.filter(test_id= data_dict['test_id']).count()
        right_counter = 0
        for i in data_dict['answers']:
            if Answer.objects.get(id=i).right_false:
                right_counter += 1


    return JsonResponse({"status": "success", "question_count": question_count, "right_counter": right_counter, "progress":right_counter*100/question_count, "is_unanswered":question_count-data_dict['counter']})







