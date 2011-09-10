# Create your views here.

from django.shortcuts import render_to_response
from django.http import Http404
from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render_to_response('polls/index.html', context)
    
# def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#   output = ', '.join([p.question for p in latest_poll_list])
#    return HttpResponse(output)

# def index(request):
#	return HttpResponse("Hello, World!  You're at the poll index.")
	
def detail(request, poll_id):
    try:
        p = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', {'poll': p})
    
# def detail(request, poll_id):
#   return HttpResponse("You're looking at poll %s." % (poll_id,))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % (poll_id,))

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % (poll_id,))