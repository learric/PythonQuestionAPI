from .models import Question

from django.views import generic

from django.http import HttpResponse

from django.core import serializers


class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()


def detail(request):
    list_details = Question.objects.all()
    data_list = serializers.serialize('json', list_details)
    return HttpResponse(data_list, content_type='application/json')
