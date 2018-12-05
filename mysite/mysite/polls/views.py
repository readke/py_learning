from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponse,HttpResponseRedirect
# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question,Choice

"""
def index(request):
    '''
        version 1:
        latest_question_list = Question.objects.order_by('-pub_data')[:5]
        output = ','.join([q.question_text for q in latest_question_list])
        return HttpResponse(output)
    '''

    '''
        version 2:
        latest_question_list = Question.objects.order_by('-pub_data')[:5]
        template = loader.get_template('polls/index.html')
        context = {'latest_question_list':latest_question_list}
        return HttpResponse(template.render(context,request))
    '''

    '''version 3:'''
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list':latest_question_list}
    #render(request对象，模板，数据)
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    '''
        version 1:
        return HttpResponse("You're looking at question %s." % question_id)
    '''

    '''
        version 2:
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request,'polls/detail.html',{'question':question})
    '''

    '''version 3:'''
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    '''
        version 1:
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)
    '''
    '''version 2:'''
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{
        'question':question
    })
"""

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return the last five published questions'''
        return Question.objects.order_by('-pub_data')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request,question_id):
    '''
        version 1:
        return HttpResponse("Your're voting on question %s." % question_id)
    '''

    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
