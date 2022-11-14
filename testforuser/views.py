from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Test


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




