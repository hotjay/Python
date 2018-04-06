from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Poll,Choice
from django.urls import  reverse
#from django.views.generic import DetailView,ListView
from django.views import generic
#from django.template import  Context,loader
# Create your views here.
# def index(req):
#     latest_poll_list =Poll.objects.order_by('-pub_date')[:5]
#     template=loader.get_template('polls/index.html')
#     context={'latest_poll_list':latest_poll_list}
#     return HttpResponse(template.render(context))


# from django.http import Http404
# def detail(req,poll_id):
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
#     return render(req,'polls/detail.html',{'poll':poll})

from django.shortcuts import get_object_or_404
def detail(req,poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    return  render(req,'polls/detail.html',{'poll':poll})
def results(req,poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    return render(req,'polls/results.html',{'poll':poll})

def vote(req,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice= p.choice_set.get(pk=req.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        render(req,'polls/detail.html',{'poll':p,'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
    return  HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

def index(req):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context={'latest_poll_list':latest_poll_list}
    return render(req,'polls/index.html',context)
####################################################################################
class IndexViews(generic.ListView):
    template_name = 'polls/index.html'
    #context_object_name = 'latest_poll_list' # 可有可无
    def get_queryset(self):
        return  Poll.objects.order_by('-pub_date')[:5]
class DetalView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(req,poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=req.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        render(req, 'polls/detail.html', {'poll': p, 'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))