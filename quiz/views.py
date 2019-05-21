from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from . models import Quiz, Question, Answer
from django.shortcuts import get_object_or_404


def alternative(request, number):
    try:
        question = Question.objects.get(quiz=2, pk=number)
        question_number = number
        while question_number > 3:
            question_number = question_number -3

    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'quiz/page.html', {'question': question, 'question_id': number,'question_number': question_number})

def page(request, number):

    try:
        question = Question.objects.get(pk=number)
        question_number = number
        while question_number >=  6:
            question_number = question_number - 5

    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'quiz/page.html', {'question': question, 'question_id': number, 'question_number': question_number})


def result(request, question_id):
   # question = get_object_or_404(Question, pk=question_id),
   question = Question.objects.get(pk=question_id)
   answer_number = question_id
   while answer_number >= 6:
       answer_number = answer_number -5

   next_one = question_id + 1


   correct_answer = ""

   for answ in Answer.objects.all():
       if answ.question_id == question_id:
           if answ.right_answer == True:
               correct_answer = answ

   try:
        selected_answer = question.answer_set.get(pk=request.POST['answer'])

   except (KeyError, Answer.DoesNotExist):
       return render(request, 'quiz/page.html', {
            'question': question,
            'error_message': "You did not select a valid choice",
        })

   else:
        if selected_answer.right_answer == True:

            context = {
                'your_answer': "Your answer is correct!",
                'question_id': question_id,
                'question': question,
                'selected_answer': selected_answer,
                'next_one': next_one,
                'answer_number': answer_number

            }
            return render(request, 'quiz/result.html', context)

        else:

            context = {
                'your_answer': "Your answer is wrong!",
                'question_id': question_id,
                'question': question,
                'selected_answer': selected_answer,
                'correct_answer': correct_answer,
                'next_one':next_one,
                'answer_number': answer_number

            }
            return render(request, 'quiz/result.html', context)





def index(request):
    return render(request, 'quiz/index.html')
    #return HttpResponse("<h2> index </h2>")