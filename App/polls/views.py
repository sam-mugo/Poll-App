from django.http import HttpResponse, response

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def detail(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
