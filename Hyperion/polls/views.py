
# Imports.
from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



def index(request):
    """
    Displays a list of all questions.

    Args:
        request (HttpRequest): The incoming request.

    Returns:
        HttpResponse: The rendered index page.
    """
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)


def detail(request, question_id):
    """
    Displays the details of a single question.

    Args:
        request (HttpRequest): The incoming request.
        question_id (int): The ID of the question.

    Returns:
        HttpResponse: The rendered detail page.
    """
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required(login_url=reverse_lazy('user_auth:login'))
def results(request, question_id):
    """
    Displays the results of a single question.

    Args:
        request (HttpRequest): The incoming request.
        question_id (int): The ID of the question.

    Returns:
        HttpResponse: The rendered results page.
    """
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required(login_url=reverse_lazy('user_auth:login'))
def vote(request, question_id):
    """
    Handles voting on a single question.

    Args:
        request (HttpRequest): The incoming request.
        question_id (int): The ID of the question.

    Returns:
        HttpResponse: The rendered vote page.
    """
    
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

