from django.shortcuts import render

# Create your views here.
def create_question(request):
    if request.method == "POST":
        pass

    else:
        return render(request, 'question/create_question.html')

