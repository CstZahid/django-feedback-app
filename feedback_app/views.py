from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def home(request):
    return render(request, 'home.html')


def feedback_view(request):
    success = False


    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
            success = True
    else:
        form = FeedbackForm()

            

    return render(request, 'feedback_form.html', {'form': form, 'success': success})

def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-id')
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})
    
