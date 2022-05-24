from django.http import JsonResponse, HttpResponseNotAllowed
from django.middleware.csrf import CsrfViewMiddleware
from django.views import generic
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from quizzes.models import Quiz
from results.models import Result


class QuizListView(generic.ListView):
    model = Quiz
    paginate_by = 10
    template_name = 'quizzes/quiz_list.html'
    context_object_name = 'quizzes'


class QuizDetailView(CsrfViewMiddleware, generic.DetailView):
    model = Quiz
    template_name = 'quizzes/quiz_detail.html'
    context_object_name = 'quiz'

    def render_to_response(self, context, **response_kwargs):
        # If request for json data, return json data
        if self.request.GET.get('format') == 'json':
            quiz: Quiz = self.object

            data = {
                'questions': [
                    {
                        'title': question.title,
                        'id': question.id,
                        'answers': [
                            {
                                'id': answer.id,
                                'title': answer.title,
                            } for answer in question.answers.all()
                        ]
                    } for question in quiz.get_questions()
                ],
                'duration': quiz.duration,
            }

            return JsonResponse(data)
        return super().render_to_response(context, **response_kwargs)

    def post(self, request, pk):
        if request.method != 'POST':
            return HttpResponseNotAllowed(['POST'])

        # if Result.objects.filter(quiz_id=pk, user=request.user).exists():
        #     msg = 'You have already taken this quiz.'
        #     return JsonResponse({'error': msg}, status=400)

        quiz = get_object_or_404(Quiz, pk=pk)
        correct_answers = 0

        right_answers_ids = []

        for question_pk, answer_pk in request.POST.items():
            try:
                question_pk = int(question_pk)
                answer_pk = int(answer_pk)
            except ValueError:
                continue

            question = get_object_or_404(quiz.questions.all(), pk=question_pk)
            answer = get_object_or_404(question.answers.all(), pk=answer_pk)

            if answer.is_correct:
                correct_answers += 1
                right_answers_ids.append(answer_pk)

        result = Result.objects.create(
            quiz=quiz,
            user=request.user,
            score=int( (correct_answers / quiz.number_of_questions) * 100),
        )

        passed_the_test = result.score >= quiz.required_score

        return JsonResponse({
            'score': result.score,
            'passed_the_test': passed_the_test,
            'right_answers_ids': right_answers_ids,
        }, status=201)
