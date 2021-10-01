from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question
import logging
logger = logging.getLogger(__name__)

# Create your views here.
##### 通常ビュー
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     #####
#     # template = loader.get_template('polls/index.html')
#     # output = template.render(context, request)
#     # return HttpResponse(output)
#     #####
#     return render(request, "polls/index.html", context)
#     #####
# 
# 
# def detail(request, question_id):
#     #####
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Wuestion does not existt")
#     #####
#     question = get_object_or_404(Question, pk=question_id)
#     #####
#     return render(request, "polls/detail.html", {"question": question})
# 
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {"question": question})
#####
##### 汎用ビュー
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects \
            .filter(pub_date__lte=timezone.now()) \
            .order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()) # pub_dateが未来の記事は参照できないようにする

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
#####

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        logger.info(selected_choice.id)
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "You didn't select a choice.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST成功時はリダイレクト
        # reverse() は ビュー名とURLパターンを引数に渡すことでURLを返す
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
