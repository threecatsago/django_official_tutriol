from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question
# Create your views here.

def index_origin(request):
    lastest_question_list = Question.objects.order_by("-pub_time")[:5]
    output = ','.join(q.questions_text for q in lastest_question_list)
    return HttpResponse(output)

def index_use_html(request):
    lastest_question_list = Question.objects.order_by("-pub_time")[:5]
    template = loader.get_template("vote/index.html")
    context = {
        "latest_question_list": lastest_question_list
    }
    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_time")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "vote/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exit")
    return render(request,'vote/detail.html',{'question':question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def voting(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
