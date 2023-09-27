from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
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
    question = get_object_or_404(Question, pk = question_id)
    results = render(request , "vote/results.html",{'question':question})
    return results


def voting(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except:
        return render(request, 'vote/detail.html',{'question':question,'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("vote:results"),args = (question.id,))

