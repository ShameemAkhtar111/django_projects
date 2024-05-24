from django.db.models import F
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_questions"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# def index(request):
#     latest_questions = Question.objects.order_by("-pub_date")[:5]
#     cont = {'latest_questions':latest_questions}
#     # template = loader.get_template("polls/index.html")
#     # return HttpResponse(template.render(context=cont, request=request))
#     return render(request,"polls/index.html", cont)

# def detail(request, ques_id):
#     # try:
#     #     q = Question.objects.get(pk=ques_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exists!!")
#     q = get_object_or_404(Question, pk=ques_id)  #either we can use try and except or this line
#     return render(request,"polls/details.html",{"question":q})

def results(request, ques_id):
    q= get_object_or_404(Question,pk=ques_id)
    return render(request,"polls/results.html",{"question":q})

def votes(request, ques_id):
    q = get_object_or_404(Question,pk=ques_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {"question":q, "error_message": "You didn't select a choice"})
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(q.id,)))

