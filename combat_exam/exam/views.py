# exam/views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Question, Answer, UserResponse
from .forms import AnswerForm
import random

def get_current_question(request):
    question_id = request.session.get('current_question', 1)
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return None
    return question

def exam_start(request):
    request.session['current_question'] = 1
    request.session['start_time'] = timezone.now()
    return redirect('exam_question')

def exam_question(request):
    question = get_current_question(request)
    if not question:
        return redirect('exam_results')

    form = AnswerForm(request.POST or None, question=question)

    if request.method == 'POST':
        if form.is_valid():
            selected_answer_id = form.cleaned_data['answer']
            selected_answer = Answer.objects.get(id=selected_answer_id)
            is_correct = selected_answer.is_correct

            UserResponse.objects.create(
                user=request.user,
                question=question,
                selected_answer=selected_answer,
                is_correct=is_correct
            )

            # Move to next question
            request.session['current_question'] += 1
            if Question.objects.filter(id=request.session['current_question']).exists():
                return redirect('exam_question')
            else:
                return redirect('exam_results')

    return render(request, 'exam/question.html', {'form': form, 'question': question})

def exam_results(request):
    responses = UserResponse.objects.filter(user=request.user)
    correct_answers = responses.filter(is_correct=True).count()

    if correct_answers > 4:
        lottery_code = f'LOTTO-{random.randint(1000, 9999)}'
        request.session['lottery_code'] = lottery_code
    else:
        request.session['lottery_code'] = None

    return render(request, 'exam/results.html', {'correct_answers': correct_answers, 'lottery_code': request.session.get('lottery_code')})
