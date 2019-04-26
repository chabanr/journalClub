from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse


from .models import Question


# Create your views here.

#
# def index(request):
#    return HttpResponse("Hello World! You're at the polls index")

# Old detail function (stub)
# def detail(request, question_id):
#     return HttpResponse("You are looking at question {:d}".format(question_id))

def detail(request, question_id):
	""" These two pieces are equivalent """
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist!")
	question = get_object_or_404(Question, pk=question_id)
	return  render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
    	selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError as e:
    	# redisplay the question voting form
    	return render(request, 'polls/detail.html', {
    		'question': question,
    		'error_message': 'You need to make a choice',
    		})
    else:
    	selected_choice.votes += 1
    	selected_choice.save()
    	# Always return an HttpResponseRedirect after successfully dealing
    	# with POST data This prevents data from being posted twice if a
    	# user hit the Back button
    	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# older listing of the questions
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	# This context dictionary maps template variable names to python objects
	context = {
		'latest_question_list':latest_question_list,
	}
	# the following two return statements are equivalent
	return render(request, 'polls/index.html', context)
	#return HttpResponse(template.render(context, request))
