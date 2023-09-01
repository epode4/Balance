from django.shortcuts import render,redirect
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm
import random

# Create your views here.

def index(request, question_id):
    question = Question.objects.get(id=question_id)

    click_all = len(question.answer_set.all())+0.1
    click_a = len(question.answer_set.all().filter(click='a'))
    click_b = len(question.answer_set.all().filter(click='b'))

    click_a_per = round(click_a/click_all * 100)
    click_b_per = round(click_b/click_all * 100)

    context = {
        'question': question,
        'click_a_per': click_a_per,
        'click_b_per': click_b_per,
    }

    return render(request, 'index.html', context)


def answer_click(request, question_id):
    
    question = Question.objects.get(id=question_id)
    answer_form = AnswerForm()

    answer = answer_form.save(commit=False)
    answer.question_id = question_id
    answer.click = (request.GET.get('choice'))

    answer.save()

    question_len = len(Question.objects.all())
    question_id = random.choice(range(1,question_len))
    return redirect('balance:index', question_id)
        
